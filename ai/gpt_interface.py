import os

import openai
from dotenv import load_dotenv

load_dotenv()  # load your .env with OPENAI_API_KEY

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("🛑 OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")

def explain_topic(topic_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful tutor who explains technical topics simply."},
            {"role": "user", "content": f"Explain this topic: {topic_text}"}
        ]
        return response["choices"][0]["message"]["content"]
    )