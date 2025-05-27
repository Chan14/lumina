import json
from datetime import datetime
from pathlib import Path

# Get the absolute path to the project's root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOURNAL_FILE = PROJECT_ROOT / "data" / "journal.json"


def load_notes():
    if JOURNAL_FILE.exists():
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_notes(notes):
    JOURNAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)


def add_note(text):
    notes = load_notes()
    note = {"timestamp": datetime.now().isoformat(), "text": text}
    notes.append(note)
    _save_notes(notes)


def show_notes():
    notes = load_notes()
    if not notes:
        print("📭 No notes yet.")
        return
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. [{note['timestamp'][:19]}]")
        print(f"   {note['text']}")
