from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from utils.gemini import get_gemini_llm

def run_risk_agent(intent, skills):
    llm = get_gemini_llm()

    def analyze_risk(_):
        return llm.invoke(f"Analyze the risk of job dissatisfaction or early quitting based on this intent:\n{intent}\nAnd these skills:\n{skills}").content

    tools = [Tool(name="RiskAnalyzer", func=analyze_risk, description="Checks for retention risk")]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    return agent.run("")
