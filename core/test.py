from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel

configure(api_key="AIzaSyA3P6n25gxBNXZw5VOOVRvGPQkVJ14TVc8")

model = GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain how AI works in one sentence.")
print(response.text)
