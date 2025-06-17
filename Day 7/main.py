import streamlit as st
from utils.agent_intent import run_intent_agent
from utils.agent_skill_map import run_skill_agent
from utils.agent_rag_match import run_rag_agent
from utils.agent_risk import run_risk_agent

st.title("Job Role Recommender (Multi-Agent AI)")

text_input = st.text_area("Paste your career statement or cover letter:")

if st.button("Analyze"):
    with st.spinner("Agent 1: Extracting Intent..."):
        intent = run_intent_agent(text_input)
        st.success(f"Career Intent:\n{intent}")

    with st.spinner("Agent 2: Mapping Skills..."):
        skills = run_skill_agent(text_input)
        st.success(f"Detected Skills:\n{skills}")

    with st.spinner("Agent 3: Matching Job Roles (RAG)..."):
        job_roles = run_rag_agent(f"{intent}, {skills}")
        st.success(f"Suggested Roles:\n{job_roles}")

    with st.spinner("Agent 4: Analyzing Risk..."):
        risk = run_risk_agent(intent, skills, job_roles)
        st.success(f"Retention Risk:\n{risk}")
