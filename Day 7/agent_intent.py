from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.gemini import llm

template = """
You are a career advisor. Extract the candidate’s career goal and desired job role from this input:

Candidate Statement:
{text}

Return a clear summary of their career intent.
"""

prompt = PromptTemplate(input_variables=["text"], template=template)

career_intent_chain = LLMChain(llm=llm, prompt=prompt)

def run_intent_agent(text):
    return career_intent_chain.run(text)
