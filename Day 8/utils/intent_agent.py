from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from utils.gemini import get_gemini_llm

def run_intent_agent(input_text):
    llm = get_gemini_llm()

    def extract_intent(text):
        return llm.invoke(f"Extract the career intent and desired role path from this text:\n{text}").content

    tools = [Tool(name="IntentExtractor", func=extract_intent, description="Extracts career goals")]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    return agent.run(input_text)
