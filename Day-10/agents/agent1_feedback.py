# agents/agent1_feedback.py

import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI

# ✅ Step 1: Load environment variables
load_dotenv()

# ✅ Step 2: Get Gemini API key from .env file
api_key =("AIzaSyDqvxncRM-pBDEmp-JHCA8awfcMS3WAPIM")

# ✅ Step 3: Define Gemini Flash LLM loader
def get_gemini_llm():
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found. Please set it in your .env file.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0.4
    )

# ✅ Step 4: Define the feedback analysis function
def extract_feedback(text: str) -> str:
    prompt = f"""
You are a UX research analyst. Analyze this testing feedback and return:

1. At least 3 critical usability issues
2. Emotional reactions (delight, frustration, confusion)
3. Grouped user suggestions

--- FEEDBACK ---
{text}
"""
    llm = get_gemini_llm()
    return llm.invoke(prompt).content

# ✅ Step 5: Define the LangChain tool
tools = [
    Tool(
        name="UXFeedbackExtractor",
        func=extract_feedback,
        description="Extracts usability problems, emotions, and user suggestions from test notes or interviews"
    )
]

# ✅ Step 6: Define the Agent executor
def run_feedback_agent(input_text: str) -> str:
    llm = get_gemini_llm()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent.run(input_text)
