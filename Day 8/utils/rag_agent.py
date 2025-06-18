from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.chains import RetrievalQA
from utils.vectorstore import create_faiss_from_pdfs
from utils.gemini import get_gemini_llm

def run_rag_agent(input_text):
    vectorstore = create_faiss_from_pdfs("data/job_roles_docs")
    retriever = vectorstore.as_retriever(search_type="similarity", k=3)
    qa = RetrievalQA.from_chain_type(llm=get_gemini_llm(), retriever=retriever)

    tools = [Tool(name="RoleMatcher", func=qa.run, description="Recommend job roles using RAG")]
    agent = initialize_agent(tools, get_gemini_llm(), agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    return agent.run(input_text)
