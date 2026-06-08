"""Command handlers for DD Engine Bot.

Each handler takes `args` (string after the command) and returns:
- dict {"type": "text", "text": "..."}                   # single text response
- dict {"type": "document", "filename": "...", "content": "...", "caption": "..."}  # file
- list of the above for multiple responses
- None for silent

Handler signature: (args: str) -> dict | list[dict] | None
"""

import datetime
import json
from pathlib import Path

import state

# ============================================================================
# Path resolution
# ============================================================================

REPO_ROOT = Path(__file__).parent.parent
SKELETONS_DIR = REPO_ROOT / "skeletons"
METHODOLOGY_DIR = REPO_ROOT / "methodology"
INTEL_DIR = REPO_ROOT / "intel"
RISK_DIR = REPO_ROOT / "risk"
BENCHMARKS_DIR = REPO_ROOT / "benchmarks"
TEMPLATES_DIR = REPO_ROOT / "templates"
KNOWLEDGE_DIR = REPO_ROOT / "knowledge"

# ============================================================================
# Sector aliases
# ============================================================================

SECTOR_ALIASES = {
    # aluminium smelter
    "al": "al_smelter",
    "al_smelter": "al_smelter",
    "aluminium": "al_smelter",
    "aluminum": "al_smelter",
    "smelter": "al_smelter",
    # aluminium downstream
    "al_downstream": "al_downstream",
    "downstream": "al_downstream",
    "casthouse": "al_downstream",
    "rolling": "al_downstream",
    "extrusion": "al_downstream",
    # nickel-PGM
    "ni": "ni_pgm",
    "ni_pgm": "ni_pgm",
    "nickel": "ni_pgm",
    "pgm": "ni_pgm",
    "norilsk": "ni_pgm",
    # gold
    "au": "gold_hydromet",
    "gold": "gold_hydromet",
    "gold_hydromet": "gold_hydromet",
    "cil": "gold_hydromet",
    "cip": "gold_hydromet",
    "tailings_reprocessing": "gold_hydromet",
    # copper
    "cu": "copper_concentrator",
    "copper": "copper_concentrator",
    "copper_concentrator": "copper_concentrator",
    "porphyry": "copper_concentrator",
    # alumina
    "alumina": "alumina_refinery",
    "alumina_refinery": "alumina_refinery",
    "bayer": "alumina_refinery",
    "bauxite": "alumina_refinery",
}

SKELETON_FILES = {
    "al_smelter": "dd_aluminium_smelter.md",
    "al_downstream": "dd_aluminium_downstream.md",
    "ni_pgm": "dd_nickel_pgm.md",
    "gold_hydromet": "dd_gold_hydromet.md",
    "copper_concentrator": "dd_copper_concentrator.md",
    "alumina_refinery": "dd_alumina_refinery.md",
}


def resolve_sector(arg):
    """Convert user input to canonical sector key. Returns None if not found."""
    if not arg:
        return None
    return SECTOR_ALIASES.get(arg.lower().strip())


# ============================================================================
# Helpers
# ============================================================================


def read_file_safe(path):
    """Read text file. Returns content or None if missing."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return None


def list_sectors_message():
    return (
        "Доступные секторы:\n"
        "• `al_smelter` — алюминиевый завод (Hall-Héroult)\n"
        "• `al_downstream` — casthouse / rolling / extrusion\n"
        "• `ni_pgm` — Cu-Ni sulphide + PGM (Norilsk-type)\n"
        "• `gold_hydromet` — золото CIL/POX/heap/tailings\n"
        "• `cu` — медный концентратор (porphyry)\n"
        "• `alumina` — глинозём (Bayer)\n\n"
        "Псевдонимы: aluminium, nickel, gold, copper, и т.д."
    )


# ============================================================================
# Command handlers
# ============================================================================


def cmd_start(args):
    return {
        "type": "text",
        "text": (
            "*DD Engine Bot* активирован.\n\n"
            "Базовые команды:\n"
            "• `/help` — полный список команд\n"
            "• `/skeleton <sector>` — выдать sector skeleton\n"
            "• `/new_dd <asset> | <sector> | <client>` — создать новый DD\n"
            "• `/list` — активные DD\n"
            "• `/intel <topic>` — intelligence file (sanctions/cbam/tailings/jorc)\n"
            "• `/killer_q <sector>` — топ killer questions\n"
            "• `/red_flags <sector>` — red flag list\n\n"
            "Phase 1b infrastructure ready. 27 файлов, 9300+ строк principal-grade."
        ),
    }


def cmd_help(args):
    return {
        "type": "text",
        "text": (
            "*DD Engine Bot — команды:*\n\n"
            "*Skeletons и intel:*\n"
            "• `/skeleton <sector>` — sector DD skeleton (файл)\n"
            "• `/intel <topic>` — intelligence file\n"
            "    topics: `sanctions`, `cbam`, `tailings`, `jorc`\n"
            "• `/method <name>` — methodology file\n"
            "    names: `fel`, `owner_team`, `workflow`, `metal_acc`\n"
            "• `/template <name>` — client template\n"
            "    names: `ic_memo`, `mgmt_session`, `red_flag_alert`\n\n"
            "*Управление DD:*\n"
            "• `/new_dd <asset> | <sector> | <client>` — создать DD\n"
            "• `/list` — все активные DD\n"
            "• `/status <id>` — детали конкретного DD\n"
            "• `/phase <id> <0-8>` — обновить фазу\n"
            "• `/note <id> <text>` — добавить заметку\n"
            "• `/done <id>` — закрыть DD\n\n"
            "*Quick reference:*\n"
            "• `/killer_q <sector>` — топ killer questions\n"
            "• `/red_flags <sector>` — sector red flags\n"
            "• `/checklist <phase>` — фаза workflow\n"
            "• `/sectors` — список секторов\n"
            "• `/ping` — проверить что бот жив"
        ),
    }


def cmd_ping(args):
    return {
        "type": "text",
        "text": f"pong · {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC",
    }


def cmd_sectors(args):
    return {"type": "text", "text": list_sectors_message()}


# --- Skeleton ---


def cmd_skeleton(args):
    sector = resolve_sector(args)
    if not sector:
        return {
            "type": "text",
            "text": "Укажи сектор: `/skeleton <sector>`.\n\n" + list_sectors_message(),
        }

    filename = SKELETON_FILES.get(sector)
    if not filename:
        return {"type": "text", "text": f"Skeleton для `{sector}` ещё не готов."}

    path = SKELETONS_DIR / filename
    content = read_file_safe(path)
    if not content:
        return {"type": "text", "text": f"Файл `{filename}` не найден на диске."}

    return {
        "type": "document",
        "filename": filename,
        "content": content,
        "caption": f"DD Skeleton — {sector}",
    }


# --- Intel ---

INTEL_FILES = {
    "sanctions": "sanctions_compliance_intel.md",
    "compliance": "sanctions_compliance_intel.md",
    "ofac": "sanctions_compliance_intel.md",
    "cbam": "cbam_carbon_intel.md",
    "carbon": "cbam_carbon_intel.md",
    "co2": "cbam_carbon_intel.md",
    "tailings": "tailings_intel.md",
    "gistm": "tailings_intel.md",
    "tsf": "tailings_intel.md",
    "jorc": "jorc_ni43101_red_flags.md",
    "ni43-101": "jorc_ni43101_red_flags.md",
    "ni43101": "jorc_ni43101_red_flags.md",
    "resources": "jorc_ni43101_red_flags.md",
    "gkz": "jorc_ni43101_red_flags.md",
}


def cmd_intel(args):
    if not args:
        return {
            "type": "text",
            "text": (
                "Укажи тему: `/intel <topic>`\n\n"
                "Доступно:\n"
                "• `sanctions` — OFAC/EU/UK/LME/LBMA matrix\n"
                "• `cbam` — EU CBAM carbon adjustment\n"
                "• `tailings` — GISTM, dams, failure modes\n"
                "• `jorc` — public report red flags, ГКЗ→CRIRSCO"
            ),
        }

    key = args.lower().strip().split()[0]
    filename = INTEL_FILES.get(key)
    if not filename:
        return {"type": "text", "text": f"Intel по `{key}` нет. /intel без аргумента — список."}

    content = read_file_safe(INTEL_DIR / filename)
    if not content:
        return {"type": "text", "text": f"Файл `{filename}` не найден."}

    return {
        "type": "document",
        "filename": filename,
        "content": content,
        "caption": f"Intel — {key}",
    }


# --- Methodology ---

METHOD_FILES = {
    "fel": "fel_methodology.md",
    "owner_team": "owner_team_engineering.md",
    "owner": "owner_team_engineering.md",
    "workflow": "dd_workflow.md",
    "dd_workflow": "dd_workflow.md",
    "metal_acc": "metal_accounting.md",
    "metal_accounting": "metal_accounting.md",
    "amira": "metal_accounting.md",
}


def cmd_method(args):
    if not args:
        return {
            "type": "text",
            "text": (
                "Methodology files:\n"
                "• `/method fel` — FEL stage gating, IC defence\n"
                "• `/method owner_team` — RUSAL casthouse signature\n"
                "• `/method workflow` — Phase 0-8 execution\n"
                "• `/method metal_acc` — AMIRA P754 metal accounting"
            ),
        }

    key = args.lower().strip().split()[0]
    filename = METHOD_FILES.get(key)
    if not filename:
        return {"type": "text", "text": f"Methodology `{key}` нет."}

    content = read_file_safe(METHODOLOGY_DIR / filename)
    if not content:
        return {"type": "text", "text": f"Файл `{filename}` не найден."}

    return {
        "type": "document",
        "filename": filename,
        "content": content,
        "caption": f"Methodology — {key}",
    }


# --- Templates ---

TEMPLATE_FILES = {
    "ic_memo": "ic_memo_template.md",
    "ic": "ic_memo_template.md",
    "mgmt_session": "management_session_protocol.md",
    "mgmt": "management_session_protocol.md",
    "session": "management_session_protocol.md",
    "red_flag_alert": "red_flag_alert_template.md",
    "red_flag": "red_flag_alert_template.md",
    "alert": "red_flag_alert_template.md",
}


def cmd_template(args):
    if not args:
        return {
            "type": "text",
            "text": (
                "Templates:\n"
                "• `/template ic_memo` — IC memo, 6-10 страниц\n"
                "• `/template mgmt_session` — management session protocol\n"
                "• `/template red_flag_alert` — mid-DD escalation"
            ),
        }

    key = args.lower().strip().split()[0]
    filename = TEMPLATE_FILES.get(key)
    if not filename:
        return {"type": "text", "text": f"Template `{key}` нет."}

    content = read_file_safe(TEMPLATES_DIR / filename)
    if not content:
        return {"type": "text", "text": f"Файл `{filename}` не найден."}

    return {
        "type": "document",
        "filename": filename,
        "content": content,
        "caption": f"Template — {key}",
    }


# --- Killer questions (extract from skeleton §16/§15/§KQ) ---


def cmd_killer_q(args):
    sector = resolve_sector(args)
    if not sector:
        return {
            "type": "text",
            "text": "Укажи сектор: `/killer_q <sector>`.\n\n" + list_sectors_message(),
        }

    filename = SKELETON_FILES.get(sector)
    if not filename:
        return {"type": "text", "text": f"Skeleton для `{sector}` нет."}

    content = read_file_safe(SKELETONS_DIR / filename)
    if not content:
        return {"type": "text", "text": f"Файл `{filename}` не найден."}

    # Extract killer questions section — find ## §N. Killer Questions ... ## §N+1
    lines = content.split("\n")
    out = []
    capture = False
    for line in lines:
        # Section heading containing "Killer Questions"
        if line.startswith("## §") and "Killer Question" in line:
            capture = True
            out.append(line)
            continue
        if capture and line.startswith("## §"):
            break  # next section
        if capture:
            out.append(line)

    if not out:
        return {"type": "text", "text": f"Killer questions section не найдена в {filename}."}

    kq_text = "\n".join(out).strip()
    return {"type": "text", "text": f"*Killer Questions — {sector}*\n\n{kq_text}"}


# --- Red flags ---


def cmd_red_flags(args):
    sector = resolve_sector(args)
    if not sector:
        # Generic — load from JSON
        path = RISK_DIR / "red_flags_decision_trees.json"
        content = read_file_safe(path)
        if not content:
            return {"type": "text", "text": "red_flags_decision_trees.json не найден."}
        return {
            "type": "document",
            "filename": "red_flags_decision_trees.json",
            "content": content,
            "caption": "Red flags — all sectors",
        }

    filename = SKELETON_FILES.get(sector)
    if not filename:
        return {"type": "text", "text": f"Skeleton для `{sector}` нет."}

    content = read_file_safe(SKELETONS_DIR / filename)
    if not content:
        return {"type": "text", "text": f"Файл `{filename}` не найден."}

    # Extract red flag checklist section
    lines = content.split("\n")
    out = []
    capture = False
    for line in lines:
        if line.startswith("## §") and "Red Flag" in line:
            capture = True
            out.append(line)
            continue
        if capture and line.startswith("## §"):
            break
        if capture:
            out.append(line)

    if not out:
        return {"type": "text", "text": f"Red Flags section не найдена в {filename}."}

    rf_text = "\n".join(out).strip()
    return {"type": "text", "text": f"*Red Flags — {sector}*\n\n{rf_text}"}


# --- Checklist (phase from dd_workflow.md) ---


def cmd_checklist(args):
    if not args:
        return {
            "type": "text",
            "text": (
                "Укажи фазу: `/checklist <0-8>`\n\n"
                + "\n".join(f"• `{n}` — {label}" for n, label in state.PHASE_LABELS.items())
            ),
        }
    try:
        phase = int(args.strip().split()[0])
    except ValueError:
        return {"type": "text", "text": "Фаза должна быть числом 0-8."}

    if phase not in state.PHASE_LABELS:
        return {"type": "text", "text": "Фаза 0-8."}

    # Extract relevant phase section from dd_workflow.md
    content = read_file_safe(METHODOLOGY_DIR / "dd_workflow.md")
    if not content:
        return {"type": "text", "text": "dd_workflow.md не найден."}

    label = state.PHASE_LABELS[phase]
    # Find heading "## 2. Phase 0", "## 3. Phase 1", etc.
    # Phases are numbered ## (phase+2). Pattern matching:
    target_section_num = phase + 2  # Phase 0 → section 2, Phase 8 → section 10
    out = []
    capture = False
    for line in content.split("\n"):
        if line.startswith(f"## {target_section_num}.") and f"Phase {phase}" in line:
            capture = True
            out.append(line)
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            out.append(line)

    if not out:
        return {
            "type": "text",
            "text": f"*Phase {phase} — {label}*\n\nДетали в `methodology/dd_workflow.md`.",
        }

    text = "\n".join(out).strip()
    if len(text) > 3500:
        return {
            "type": "document",
            "filename": f"phase_{phase}_checklist.md",
            "content": text,
            "caption": f"Phase {phase} — {label}",
        }
    return {"type": "text", "text": text}


# --- DD lifecycle ---


def cmd_new_dd(args):
    if not args or "|" not in args:
        return {
            "type": "text",
            "text": (
                "Формат: `/new_dd <asset> | <sector> | <client>`\n\n"
                "Пример: `/new_dd Smelter X, Karaganda | al_smelter | PE Fund Y`\n\n"
                "Опционально: добавь `| Deep` в конце для Deep DD (default Standard)."
            ),
        }

    parts = [p.strip() for p in args.split("|")]
    if len(parts) < 3:
        return {"type": "text", "text": "Нужно 3 поля минимум: asset | sector | client."}

    asset, sector_raw, client = parts[0], parts[1], parts[2]
    scope = parts[3] if len(parts) > 3 else "Standard"

    sector = resolve_sector(sector_raw)
    if not sector:
        return {
            "type": "text",
            "text": f"Сектор `{sector_raw}` не распознан.\n\n" + list_sectors_message(),
        }

    dds = state.load_active_dds()
    dd_id = state.next_dd_id(dds)
    today = datetime.date.today().isoformat()

    dd = {
        "id": dd_id,
        "asset": asset,
        "sector": sector,
        "client": client,
        "scope": scope,
        "started": today,
        "phase": 0,
        "phase_label": state.PHASE_LABELS[0],
        "deadline": None,
        "notes": [],
        "next_action": "Sign SoW, NDA, MSA. Define Phase 0 deliverables.",
    }
    state.upsert_dd(dd)

    return {
        "type": "text",
        "text": (
            f"✅ *DD {dd_id}* создан.\n\n"
            f"• *Asset:* {asset}\n"
            f"• *Sector:* `{sector}`\n"
            f"• *Client:* {client}\n"
            f"• *Scope:* {scope}\n"
            f"• *Started:* {today}\n"
            f"• *Phase:* 0 — {state.PHASE_LABELS[0]}\n\n"
            f"Next action: {dd['next_action']}\n\n"
            f"Команды: `/status {dd_id}`, `/phase {dd_id} 1`, `/note {dd_id} ...`"
        ),
    }


def cmd_list(args):
    dds = state.load_active_dds()
    if not dds:
        return {"type": "text", "text": "Активных DD нет.\n\n`/new_dd <asset> | <sector> | <client>` чтобы создать."}

    lines = [f"*Активных DD: {len(dds)}*\n"]
    for dd_id, dd in sorted(dds.items()):
        lines.append(
            f"`{dd_id}` · *{dd['asset']}*\n"
            f"  Sector: {dd['sector']} · Client: {dd['client']} · Scope: {dd['scope']}\n"
            f"  Phase {dd['phase']}/8 · {dd['phase_label']} · started {dd['started']}\n"
            f"  Next: {dd.get('next_action', '—')}"
        )
    return {"type": "text", "text": "\n\n".join(lines)}


def cmd_status(args):
    if not args:
        return {"type": "text", "text": "Формат: `/status <dd-id>`. Список: `/list`."}

    dd_id = args.strip().split()[0].lower()
    dd = state.get_dd(dd_id)
    if not dd:
        return {"type": "text", "text": f"DD `{dd_id}` не найден. `/list` для списка."}

    notes_text = ""
    if dd.get("notes"):
        notes_text = "\n*Notes:*\n" + "\n".join(f"• {n}" for n in dd["notes"][-10:])

    return {
        "type": "text",
        "text": (
            f"*DD {dd['id']}*\n\n"
            f"• Asset: *{dd['asset']}*\n"
            f"• Sector: `{dd['sector']}`\n"
            f"• Client: {dd['client']}\n"
            f"• Scope: {dd['scope']}\n"
            f"• Started: {dd['started']}\n"
            f"• Phase: *{dd['phase']}/8* — {dd['phase_label']}\n"
            f"• Deadline: {dd.get('deadline') or '—'}\n"
            f"• Next action: {dd.get('next_action', '—')}"
            f"{notes_text}"
        ),
    }


def cmd_phase(args):
    parts = args.strip().split()
    if len(parts) < 2:
        return {"type": "text", "text": "Формат: `/phase <dd-id> <0-8>`."}

    dd_id = parts[0].lower()
    try:
        new_phase = int(parts[1])
    except ValueError:
        return {"type": "text", "text": "Фаза 0-8."}

    if new_phase not in state.PHASE_LABELS:
        return {"type": "text", "text": "Фаза 0-8."}

    dd = state.get_dd(dd_id)
    if not dd:
        return {"type": "text", "text": f"DD `{dd_id}` не найден."}

    old_phase = dd["phase"]
    dd["phase"] = new_phase
    dd["phase_label"] = state.PHASE_LABELS[new_phase]
    state.upsert_dd(dd)

    return {
        "type": "text",
        "text": (
            f"✅ `{dd_id}` Phase {old_phase} → *{new_phase}* ({state.PHASE_LABELS[new_phase]})"
        ),
    }


def cmd_note(args):
    parts = args.strip().split(maxsplit=1)
    if len(parts) < 2:
        return {"type": "text", "text": "Формат: `/note <dd-id> <text>`."}

    dd_id, text = parts[0].lower(), parts[1]
    dd = state.get_dd(dd_id)
    if not dd:
        return {"type": "text", "text": f"DD `{dd_id}` не найден."}

    timestamped = f"[{datetime.date.today().isoformat()}] {text}"
    dd.setdefault("notes", []).append(timestamped)
    state.upsert_dd(dd)

    return {"type": "text", "text": f"✓ Note добавлен к `{dd_id}`."}


def cmd_done(args):
    if not args:
        return {"type": "text", "text": "Формат: `/done <dd-id>`."}

    dd_id = args.strip().split()[0].lower()
    dd = state.get_dd(dd_id)
    if not dd:
        return {"type": "text", "text": f"DD `{dd_id}` не найден."}

    removed = state.delete_dd(dd_id)
    return {
        "type": "text",
        "text": (
            f"✅ DD `{dd_id}` закрыт.\n\n"
            f"*{removed['asset']}* — Phase {removed['phase']}/8.\n"
            f"Не забудь обновить `lessons_learned.md` и `anton_cases.json`."
        ),
    }


# --- Catch-all ---


def cmd_unknown(args):
    return {
        "type": "text",
        "text": "Не знаю такой команды. `/help` для списка.",
    }


def cmd_note_freeform(args):
    """For non-command messages — silent (could be expanded to capture as notes)."""
    return None


# ============================================================================
# Handler registry
# ============================================================================

HANDLERS = {
    "start": cmd_start,
    "help": cmd_help,
    "ping": cmd_ping,
    "sectors": cmd_sectors,
    "skeleton": cmd_skeleton,
    "skel": cmd_skeleton,
    "intel": cmd_intel,
    "method": cmd_method,
    "methodology": cmd_method,
    "template": cmd_template,
    "killer_q": cmd_killer_q,
    "kq": cmd_killer_q,
    "red_flags": cmd_red_flags,
    "rf": cmd_red_flags,
    "checklist": cmd_checklist,
    "new_dd": cmd_new_dd,
    "newdd": cmd_new_dd,
    "list": cmd_list,
    "list_dd": cmd_list,
    "ls": cmd_list,
    "status": cmd_status,
    "phase": cmd_phase,
    "note": cmd_note,
    "done": cmd_done,
    "close": cmd_done,
    # non-command messages go silent (no spam if Anton types non-command text)
    "note_freeform": cmd_note_freeform,
}
