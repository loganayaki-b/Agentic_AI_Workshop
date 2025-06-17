from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from utils.gemini import llm

def load_vectorstore():
    loader = PyPDFLoader("data/roles.pdf")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.from_documents(texts, embeddings)
    db.save_local("vectorstore")
    return db

def run_rag_agent(query):
    db = FAISS.load_local("vectorstore", GoogleGenerativeAIEmbeddings(model="models/embedding-001"), allow_dangerous_deserialization=True)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa.run(query)
