#!/usr/bin/env python3
"""Daily DD status pusher.

Runs once per morning (09:00 MSK Mon-Fri).
Sends a summary of active DDs and overdue actions to Telegram.
"""

import datetime
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import state

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    print("ERROR: missing env vars")
    sys.exit(1)


def send_text(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode(
        {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": "true",
        }
    ).encode()
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Send error: {e}")
        return None


def main():
    dds = state.load_active_dds()
    today = datetime.date.today().isoformat()

    if not dds:
        send_text(
            f"🌅 *DD Engine — {today}*\n\n"
            f"Активных DD нет.\n\n"
            f"`/new_dd <asset> | <sector> | <client>` чтобы создать."
        )
        return 0

    lines = [f"🌅 *DD Engine — {today}*\n", f"Активных DD: *{len(dds)}*\n"]

    # Phase distribution
    by_phase = {}
    for dd in dds.values():
        by_phase.setdefault(dd["phase"], []).append(dd)

    for phase in sorted(by_phase.keys()):
        phase_label = state.PHASE_LABELS.get(phase, "?")
        lines.append(f"\n*Phase {phase} — {phase_label}* ({len(by_phase[phase])})")
        for dd in by_phase[phase]:
            deadline_marker = ""
            if dd.get("deadline"):
                try:
                    d = datetime.date.fromisoformat(dd["deadline"])
                    days_left = (d - datetime.date.today()).days
                    if days_left < 0:
                        deadline_marker = f" ⚠️ просрочка {-days_left}д"
                    elif days_left <= 3:
                        deadline_marker = f" 🔥 {days_left}д до дедлайна"
                except ValueError:
                    pass
            lines.append(
                f"• `{dd['id']}` *{dd['asset']}* ({dd['client']}){deadline_marker}\n"
                f"  Next: {dd.get('next_action', '—')}"
            )

    lines.append("\n`/list` — детали · `/help` — команды")
    send_text("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
