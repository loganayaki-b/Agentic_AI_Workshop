import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def create_faiss_from_pdfs(directory):
    documents = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            with open(os.path.join(directory, filename), "rb") as f:
                from PyPDF2 import PdfReader
                pdf = PdfReader(f)
                raw_text = ""
                for page in pdf.pages:
                    raw_text += page.extract_text()
                chunks = splitter.split_text(raw_text)
                documents.extend([Document(page_content=c) for c in chunks])

    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore
