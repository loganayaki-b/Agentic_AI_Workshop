import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load your API key from .env file
load_dotenv()

# Access the Gemini API key
GOOGLE_API_KEY = ("AIzaSyBsYKqPb7sKXv68s855ro5o05YbkNEgpgU")

# Raise error if key is missing
if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file!")

# Create the Gemini Flash LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",       # or "gemini-2.0-flash" if supported
    temperature=0.3,
    convert_system_message_to_human=True
)
