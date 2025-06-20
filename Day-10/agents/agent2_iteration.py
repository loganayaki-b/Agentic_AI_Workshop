from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

# 🔁 Gemini Flash Loader
def get_gemini_llm():
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=("AIzaSyCFbKhsHWc0lhEqXgfeO9I3bQy637cMTVA"))

# 🧠 Tool Function
def generate_iteration_plan(feedback_summary: str) -> str:
    prompt = f"""
    You are a UX iteration strategist.

Your task:
- Analyze the given user feedback summary.
- Recommend 3 to 5 **clear improvements** in the following markdown format:

FORMAT (strictly follow):
1. **[Improvement Title]**
   - Component: ...
   - Type: Enhancement / Redesign / Removal
   - Reason: ...

📍 Design Cycle Checkpoints
- List 2 to 3 steps for testing or validating the changes.

--- FEEDBACK SUMMARY ---
{feedback_summary}
    --- FEEDBACK SUMMARY ---
    {feedback_summary}
    """
    llm = get_gemini_llm()
    return llm.invoke(prompt).content

# 🛠️ LangChain Tool
tools = [
    Tool(
        name="IterationPlanner",
        func=generate_iteration_plan,
        description="Plans top 3–5 improvements from a feedback summary"
    )
]

# 🚀 Agent Runner
def run_iteration_agent(feedback_summary: str) -> str:
    llm = get_gemini_llm()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent.run(feedback_summary)
