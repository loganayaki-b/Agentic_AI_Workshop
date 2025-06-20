import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyC1L3hEamEkg6_xN4LSUm7yHsjfaKTQPf4")

def get_gemini_llm():
    if not GEMINI_API_KEY:
        raise ValueError("❌ GEMINI_API_KEY not found in .env file.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.3
    )
