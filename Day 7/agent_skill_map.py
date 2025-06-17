from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.gemini import llm

template = """
You are a technical evaluator. Given this candidate's input, extract technical and soft skills. Include inferred skills too.

Candidate Statement:
{text}

List skills in bullet points.
"""

prompt = PromptTemplate(input_variables=["text"], template=template)
skill_chain = LLMChain(llm=llm, prompt=prompt)

def run_skill_agent(text):
    return skill_chain.run(text)
