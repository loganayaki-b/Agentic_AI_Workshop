from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from utils.gemini import get_gemini_llm

def run_skill_agent(intent, input_text):
    llm = get_gemini_llm()

    def extract_skills(text):
        return llm.invoke(f"Based on this profile:\n{text}\n\nMatch the skills to this intent:\n{intent}").content

    tools = [Tool(name="SkillMapper", func=extract_skills, description="Matches skills to intent")]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    return agent.run(input_text)
