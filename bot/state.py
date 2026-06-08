"""State persistence for DD Engine Bot.

State is stored as JSON files in data/ folder.
GitHub Actions workflow commits these back to the repo at end of run.

Files:
- data/last_update_id.json — Telegram update_id offset to avoid replay
- data/active_dds.json — registry of in-progress DD engagements
"""

import json
from pathlib import Path

# Base path resolved relative to this file (bot/state.py → ../data/)
DATA_DIR = Path(__file__).parent.parent / "data"
LAST_UPDATE_FILE = DATA_DIR / "last_update_id.json"
ACTIVE_DDS_FILE = DATA_DIR / "active_dds.json"


def _ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Last update ID (Telegram getUpdates offset)
# ---------------------------------------------------------------------------


def load_last_update_id():
    _ensure_data_dir()
    if not LAST_UPDATE_FILE.exists():
        return 0
    try:
        with open(LAST_UPDATE_FILE) as f:
            return int(json.load(f).get("last_update_id", 0))
    except (json.JSONDecodeError, ValueError, OSError):
        return 0


def save_last_update_id(update_id):
    _ensure_data_dir()
    with open(LAST_UPDATE_FILE, "w") as f:
        json.dump({"last_update_id": int(update_id)}, f, indent=2)


# ---------------------------------------------------------------------------
# Active DDs registry
# ---------------------------------------------------------------------------

# Schema for an active DD:
# {
#   "id": "dd-001",
#   "asset": "Aluminium Smelter X, Kazakhstan",
#   "sector": "al_smelter",
#   "client": "PE Fund Y",
#   "scope": "Standard",          # Standard / Deep
#   "started": "2026-06-08",
#   "phase": 0,                    # 0..8 per dd_workflow.md
#   "phase_label": "Scoping",
#   "deadline": "2026-07-15",
#   "notes": ["..."],
#   "next_action": "...",
# }


PHASE_LABELS = {
    0: "Scoping & contract",
    1: "Document review",
    2: "Public research",
    3: "Management session",
    4: "Site visit",
    5: "Specialist input",
    6: "Synthesis & risk register",
    7: "Report & IC memo",
    8: "Client review & delivery",
}


def load_active_dds():
    _ensure_data_dir()
    if not ACTIVE_DDS_FILE.exists():
        return {}
    try:
        with open(ACTIVE_DDS_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_active_dds(dds):
    _ensure_data_dir()
    with open(ACTIVE_DDS_FILE, "w") as f:
        json.dump(dds, f, indent=2, ensure_ascii=False)


def next_dd_id(dds):
    """Generate next available DD ID like dd-001, dd-002, ..."""
    if not dds:
        return "dd-001"
    nums = []
    for k in dds.keys():
        if k.startswith("dd-"):
            try:
                nums.append(int(k.split("-", 1)[1]))
            except (ValueError, IndexError):
                pass
    next_num = (max(nums) if nums else 0) + 1
    return f"dd-{next_num:03d}"


def get_dd(dd_id):
    dds = load_active_dds()
    return dds.get(dd_id)


def upsert_dd(dd):
    dds = load_active_dds()
    dds[dd["id"]] = dd
    save_active_dds(dds)
    return dd


def delete_dd(dd_id):
    dds = load_active_dds()
    removed = dds.pop(dd_id, None)
    save_active_dds(dds)
    return removed
