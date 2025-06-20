from .vectorstore import build_pdf_vectorstore
from sentence_transformers import SentenceTransformer

def retrieve_from_pdf(query, pdf_path="startup_data/unicorns_5_domains.pdf", top_k=3):

    index, vectors, docs = build_pdf_vectorstore(pdf_path)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec = model.encode([query])
    D, I = index.search(query_vec, top_k)
    return [docs[i] for i in I[0]]


