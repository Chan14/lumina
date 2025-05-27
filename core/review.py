# core/review.py

from datetime import datetime, timedelta

from core.gemini_client import model  # ✅ shared Gemini model
from core.goals import load_goals
from core.journal import load_notes
from core.user import load_user_info


def filter_recent_notes(days=7):
    notes = load_notes()
    cutoff = datetime.now() - timedelta(days=days)
    recent = [
        note for note in notes if datetime.fromisoformat(note["timestamp"]) >= cutoff
    ]
    return recent


def generate_study_review_gemini(days=7, sub_prompt=None):
    recent_notes = filter_recent_notes(days)
    goals = load_goals()
    user_info = load_user_info()

    if not recent_notes:
        return f"You have no notes from the past {days} days."

    notes_text = "\n".join(
        f"{note['timestamp']}: {note['text']}" for note in recent_notes
    )

    goals_text = (
        "\n".join(
            f"- {goal['title']}: {goal.get('description', 'No description')}"
            for goal in goals
        )
        if goals
        else "No long-term goals set."
    )

    prompt = f"""
You are Lumina, a wise, encouraging AI mentor.

User Data:
{user_info}


Here are the user’s recent learning notes from the past {days} days:
{notes_text}


Here are the user’s current long-term learning goals:
{goals_text}
"""
    if sub_prompt:
        prompt += f"\n{sub_prompt}\n"

    prompt += """

Please do the following:
1. Summarize what the user has been learning.
2. Suggest key areas to explore next, based on both recent focus and long-term goals.
3. Reflect briefly on how this connects to the user’s overarching aspirations.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini encountered a problem: {e}"
