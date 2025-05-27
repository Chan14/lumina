import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel

from core.goals import load_goals
from core.journal import load_notes

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# ✅ configure the Gemini client
configure(api_key=api_key)


def filter_recent_notes(days=7):
    notes = load_notes()
    cutoff = datetime.now() - timedelta(days=days)
    recent = [
        note for note in notes if datetime.fromisoformat(note["timestamp"]) >= cutoff
    ]
    return recent


def generate_study_review_gemini(days: int = 7):
    recent_notes = filter_recent_notes(days)

    if not recent_notes:
        return f"You have no notes from the past {days} days."

    notes_text = "\n".join(
        f"{note['timestamp']}: {note['text']}" for note in recent_notes
    )

    prompt = f"""
You are Lumina, a wise, encouraging AI mentor.

Here are the user’s recent learning notes from the past {days} days:

{notes_text}

Please do the following:
1. Summarize what the user has been learning.
2. Suggest 1–2 key areas to explore next, based on their recent focus.
3. Reflect briefly on how this connects to the user’s long-term learning goals.
"""

    try:
        model = GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini encountered a problem: {e}"
