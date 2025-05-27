import json
import os
from datetime import datetime
from pathlib import Path

# Get the absolute path to the project's root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
GOALS_FILE = PROJECT_ROOT / "data" / "goals.json"


def load_goals():
    try:
        with open(GOALS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save_goals(goals):
    with open(GOALS_FILE, "w", encoding="utf-8") as f:
        json.dump(goals, f, indent=2)


def add_goal(title, description=""):
    goals = load_goals()
    new_goal = {
        "title": title.strip(),
        "description": description.strip(),
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    goals.append(new_goal)
    _save_goals(goals)
    print(f"✅ Goal added: {title}")


def list_goals():
    goals = load_goals()
    if not goals:
        print("📭 No goals set yet.")
        return
    for i, goal in enumerate(goals, 1):
        print(f"\n{i}. {goal['title']}")
        if goal["description"]:
            print(f"   {goal['description']}")
        print(f"   Created on: {goal['created']}")
