# core/gemini_client.py
import os

from dotenv import load_dotenv
from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel

load_dotenv()

# Exposed constants
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = "gemini-1.5-flash"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

configure(api_key=GEMINI_API_KEY)

# Shared Gemini model instance
model = GenerativeModel(GEMINI_MODEL_NAME)
