from sentence_transformers import SentenceTransformer
import faiss
from utils.pdf_reader import extract_text_from_pdf

def load_pdf_chunks(pdf_path):
    full_text = extract_text_from_pdf(pdf_path)
    chunks = [chunk.strip() for chunk in full_text.split("\n") if len(chunk.strip()) > 30]
    return chunks

def build_pdf_vectorstore(pdf_path="startup_data/unicorns_5_domains.pdf"):
    data = load_pdf_chunks(pdf_path)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(data)
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings, data
