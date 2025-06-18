import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.intent_agent import run_intent_agent
from utils.skill_agent import run_skill_agent
from utils.rag_agent import run_rag_agent
from utils.risk_agent import run_risk_agent

st.set_page_config(page_title="Job Role Recommender", layout="wide")
st.title("🧠 AI-Powered Job Role Recommender")

uploaded_file = st.file_uploader("Upload your Resume/Career Intent PDF", type="pdf")

if uploaded_file:
    with st.spinner("Reading PDF..."):
        input_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📌 Extracted Career Intent")
    career_intent = run_intent_agent(input_text)
    st.success(career_intent)

    st.subheader("📌 Skill & Aspiration Mapping")
    skill_match = run_skill_agent(career_intent, input_text)
    st.success(skill_match)

    st.subheader("📌 Recommended Job Roles (RAG-Based)")
    job_roles = run_rag_agent(input_text)
    st.success(job_roles)

    st.subheader("📌 Retention Risk Analysis")
    risk = run_risk_agent(career_intent, skill_match)
    st.warning(risk)
