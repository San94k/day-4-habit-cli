import json
from pathlib import Path

DB_DIR = Path("data")
DB_PATH = DB_DIR / "habits.json"

def _ensure():
    DB_DIR.mkdir(exist_ok=True)
    if not DB_PATH.exists():
        DB_PATH.write_text("[]", encoding="utf-8")

def load_data():
    _ensure()
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_data(data):
    _ensure()
    DB_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
