from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.gemini import llm

template = """
Given the candidate's career intent and skills, analyze how well they align with the recommended job roles.

Intent: {intent}
Skills: {skills}
Suggested Roles: {roles}

Output a risk level (Low, Medium, High) and a brief explanation.
"""

prompt = PromptTemplate(input_variables=["intent", "skills", "roles"], template=template)
risk_chain = LLMChain(llm=llm, prompt=prompt)

def run_risk_agent(intent, skills, roles):
    return risk_chain.run({"intent": intent, "skills": skills, "roles": roles})
