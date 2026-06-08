#!/usr/bin/env python3
"""DD Engine Bot — Telegram interface for Anton Zaytsev's DD Production Line.

Architecture: GitHub Actions runs this script every 5 minutes.
- Polls Telegram getUpdates with last_update_id offset
- Dispatches commands to handlers in commands.py
- Saves state (active DDs, last_update_id) to data/ folder
- Workflow commits state back to repo at end of run

No external dependencies. Pure Python stdlib.

Environment variables required:
- TELEGRAM_BOT_TOKEN — from @BotFather for @DD_engine_bot
- TELEGRAM_CHAT_ID — 849676420 (Anton's chat, authorized user)

Optional:
- DEEPSEEK_API_KEY — for /research command (Phase 2 feature)
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

# Add bot folder to path so we can import sibling modules
sys.path.insert(0, str(Path(__file__).parent))

import commands
import state

# ============================================================================
# Configuration
# ============================================================================

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    print("ERROR: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in environment")
    sys.exit(1)

AUTHORIZED_CHAT_ID = int(TELEGRAM_CHAT_ID)
API_BASE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

# ============================================================================
# Telegram API helpers
# ============================================================================


def tg_request(method, params=None, files=None):
    """Make a Telegram Bot API request. Returns parsed JSON response."""
    url = f"{API_BASE}/{method}"

    if files:
        # Multipart form for file uploads (sendDocument)
        boundary = "----DDEngineBoundary7890ABCDEF"
        body_parts = []

        for key, value in (params or {}).items():
            body_parts.append(f"--{boundary}".encode())
            body_parts.append(
                f'Content-Disposition: form-data; name="{key}"'.encode()
            )
            body_parts.append(b"")
            body_parts.append(str(value).encode("utf-8"))

        for field_name, (filename, file_bytes, content_type) in files.items():
            body_parts.append(f"--{boundary}".encode())
            body_parts.append(
                f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"'.encode()
            )
            body_parts.append(f"Content-Type: {content_type}".encode())
            body_parts.append(b"")
            body_parts.append(file_bytes)

        body_parts.append(f"--{boundary}--".encode())
        body_parts.append(b"")
        body = b"\r\n".join(body_parts)

        req = urllib.request.Request(
            url,
            data=body,
            headers={
                "Content-Type": f"multipart/form-data; boundary={boundary}"
            },
        )
    else:
        data = urllib.parse.urlencode(params or {}).encode()
        req = urllib.request.Request(url, data=data)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code} on {method}: {body[:500]}")
        return {"ok": False, "error": body}
    except Exception as e:
        print(f"Exception on {method}: {e}")
        return {"ok": False, "error": str(e)}


def get_updates(offset):
    """Poll for new messages. Returns list of update dicts."""
    resp = tg_request(
        "getUpdates",
        {"offset": offset, "timeout": 1, "allowed_updates": json.dumps(["message"])},
    )
    if not resp.get("ok"):
        print(f"getUpdates failed: {resp.get('error', 'unknown')}")
        return []
    return resp.get("result", [])


def send_message(text, parse_mode="Markdown", reply_to=None):
    """Send a text message. Auto-handles 4096 char limit by splitting."""
    MAX_LEN = 4000

    # Split if needed
    if len(text) <= MAX_LEN:
        chunks = [text]
    else:
        chunks = []
        while text:
            if len(text) <= MAX_LEN:
                chunks.append(text)
                break
            # Find last newline within limit
            cut = text.rfind("\n", 0, MAX_LEN)
            if cut == -1:
                cut = MAX_LEN
            chunks.append(text[:cut])
            text = text[cut:].lstrip("\n")

    last_result = None
    for chunk in chunks:
        params = {
            "chat_id": AUTHORIZED_CHAT_ID,
            "text": chunk,
            "parse_mode": parse_mode,
            "disable_web_page_preview": "true",
        }
        if reply_to:
            params["reply_to_message_id"] = reply_to
            reply_to = None  # Only first chunk replies

        last_result = tg_request("sendMessage", params)
        if not last_result.get("ok"):
            # Try without parse_mode (markdown parsing errors common)
            params.pop("parse_mode", None)
            last_result = tg_request("sendMessage", params)

    return last_result


def send_document(filename, content, caption=None):
    """Send a file. content can be str or bytes."""
    if isinstance(content, str):
        content = content.encode("utf-8")

    params = {"chat_id": AUTHORIZED_CHAT_ID}
    if caption:
        params["caption"] = caption[:1024]  # Telegram caption limit

    files = {"document": (filename, content, "text/markdown; charset=utf-8")}
    return tg_request("sendDocument", params, files=files)


# ============================================================================
# Command dispatcher
# ============================================================================


def dispatch(message):
    """Route incoming message to appropriate command handler."""
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "").strip()
    message_id = message.get("message_id")

    # Authorization: only respond to Anton's chat
    if chat_id != AUTHORIZED_CHAT_ID:
        print(f"Ignored message from unauthorized chat {chat_id}")
        return

    if not text:
        return

    # Parse command and args
    if text.startswith("/"):
        parts = text.split(maxsplit=1)
        cmd = parts[0].lower().lstrip("/").split("@")[0]  # /cmd or /cmd@botname
        args = parts[1] if len(parts) > 1 else ""
    else:
        # Non-command messages — treat as note/query
        cmd = "note"
        args = text

    print(f"Command: /{cmd}, args: {args[:100]}")

    handler = commands.HANDLERS.get(cmd, commands.cmd_unknown)
    try:
        response = handler(args)
    except Exception as e:
        response = {
            "type": "text",
            "text": f"⚠️ Ошибка в /{cmd}: `{type(e).__name__}: {e}`",
        }
        print(f"Handler exception: {e}")
        import traceback
        traceback.print_exc()

    # Process handler response
    if response is None:
        return

    if isinstance(response, list):
        responses = response
    else:
        responses = [response]

    for r in responses:
        rtype = r.get("type", "text")
        if rtype == "text":
            send_message(r["text"], parse_mode=r.get("parse_mode", "Markdow
