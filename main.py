# main.py
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-2.5-pro")

def ask_gemini(prompt):
    """Send a prompt to Gemini and return its text response."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR] {e}"

if __name__ == "__main__":
    print("🚀 Geminaut Mission Control Online.")
    while True:
        user_input = input("🛰 Command: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("🤖 Gemini:", ask_gemini(user_input))
