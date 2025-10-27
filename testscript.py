# gemini_test.py
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a model
model = genai.GenerativeModel("models/gemini-2.5-pro")

# Test prompt
response = model.generate_content("Hello from the Geminaut project at Constructor University!")
print(response.text)
