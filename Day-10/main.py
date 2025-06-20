import streamlit as st
from agents.agent1_feedback import run_feedback_agent
from agents.agent2_iteration import run_iteration_agent
from agents.agent3_validator import run_validator_agent
from agents.agent4_pitch import run_pitch_agent
from agents.agent5_docs import run_documentation_agent

from utils.file_handler import extract_text_from_pdf
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
import json
import pdfkit
import os
import tempfile

st.set_page_config(page_title="Agentic Testing Assistant", layout="wide")
st.title("🧪 Agentic AI-Powered Testing Assistant")

# ---------------------- Shared File Upload ----------------------
uploaded_file = st.file_uploader("Upload user testing notes or interview transcript", type=["txt", "pdf"]) 

if uploaded_file:
    st.success("File uploaded successfully!")

    # 📄 Extract content
    if uploaded_file.type == "application/pdf":
        content = extract_text_from_pdf(uploaded_file)
    else:
        content = uploaded_file.read().decode("utf-8")

    # ---------------------- AGENT 1 ----------------------
    if st.button("Run Feedback Analysis Agent (Agent 1)"):
        with st.spinner("Analyzing feedback..."):
            feedback_summary = run_feedback_agent(content)
        st.subheader("🧠 Feedback Summary (Agent 1):")
        st.write(feedback_summary)
        st.session_state["agent1_output"] = feedback_summary

    # ---------------------- AGENT 2 ----------------------
    if "agent1_output" in st.session_state:
        if st.button("Run Iteration Planner Agent (Agent 2)"):
            with st.spinner("Generating iteration plan..."):
                iteration_plan = run_iteration_agent(st.session_state["agent1_output"])
            st.subheader("🛠️ Iteration Plan (Agent 2):")
            st.write(iteration_plan)
            st.session_state["agent2_output"] = iteration_plan
    else:
        st.info("ℹ️ Please run Agent 1 first to enable Agent 2.")

# ---------------------- AGENT 3: INNOVATION VALIDATOR ----------------------
st.markdown("---")
st.subheader("📘 Innovation Validator Agent (Agent 3)")

# 🔧 Static unicorn RAG PDF path (no file uploader)
rag_pdf = "startup data/unicorns_5_domains.pdf"  # Make sure this path is correct

# 📝 Enter project idea
project_description = st.text_area("Enter your final project idea for evaluation:", height=180)

if st.button("Run Innovation Validator Agent (Agent 3)"):
    if not project_description.strip():
        st.warning("⚠️ Please enter a project idea.")
    else:
        with st.spinner("Validating innovation..."):
            try:
                result = run_validator_agent(project_description, rag_pdf)
                st.success("✅ Innovation scorecard generated!")
                st.subheader("📊 Innovation Scorecard (Agent 3):")
                st.markdown(result, unsafe_allow_html=True)
                st.session_state["agent3_output"] = result
            except Exception as e:
                st.error(f"❌ Error: {e}")


# ---------------------- AGENT 4: PITCH GENERATOR ----------------------
# ---------------------- AGENT 4: PITCH GENERATOR ----------------------
st.subheader("🎤 Pitch Generator Agent (Agent 4)")

if (
    "agent1_output" in st.session_state and
    "agent2_output" in st.session_state and
    "agent3_output" in st.session_state and
    project_description.strip()
):
    if st.button("Run Pitch Generator Agent (Agent 4)"):
        with st.spinner("Generating your pitch..."):
            from agents.agent4_pitch import run_pitch_agent
            pitch = run_pitch_agent(
                project_description,
                st.session_state["agent1_output"],
                st.session_state["agent2_output"],
                st.session_state["agent3_output"]
            )
        st.success("✅ Startup Pitch Ready!")
        st.markdown(pitch, unsafe_allow_html=True)
        st.session_state["agent4_output"] = pitch
else:
    st.info("ℹ️ Run Agents 1–3 and enter project idea to enable Pitch Agent.")


# ---------------------- AGENT 5: LAUNCH READINESS ----------------------
# ---------------------- AGENT 5: Documentation & Branding Agent ----------------------
st.markdown("---")
st.subheader("📄 Final Documentation & Branding Agent (Agent 5)")

if (
    "agent1_output" in st.session_state and
    "agent2_output" in st.session_state and
    "agent3_output" in st.session_state and
    "agent4_output" in st.session_state and
    project_description.strip()
):
    if st.button("📦 Generate Documentation & Branding (Agent 5)"):
        with st.spinner("Generating booklet, LinkedIn, and GitHub docs..."):
            from agents.agent5_docs import run_documentation_agent
            doc_result = run_documentation_agent(
                project_description,
                st.session_state["agent1_output"],
                st.session_state["agent2_output"],
                st.session_state["agent3_output"],
                st.session_state["agent4_output"]
            )
        st.success("✅ Documentation and branding assets ready!")

        # 📘 Case Booklet Download
        with open(doc_result["case_booklet_md"], "r", encoding="utf-8") as f:
            st.download_button(
                label="📘 Download Case Booklet (Markdown)",
                data=f.read(),
                file_name="case_booklet.md",
                mime="text/markdown"
            )

        # 💼 LinkedIn Post Download
        with open(doc_result["linkedin_post"], "r", encoding="utf-8") as f:
            st.download_button(
                label="💼 Download LinkedIn Post",
                data=f.read(),
                file_name="linkedin_post.txt",
                mime="text/plain"
            )

        # 🛠️ GitHub README Download
        with open(doc_result["github_readme"], "r", encoding="utf-8") as f:
            st.download_button(
                label="🛠️ Download GitHub README",
                data=f.read(),
                file_name="README.md",
                mime="text/markdown"
            )
else:
    st.info("ℹ️ Run Agents 1–4 and enter project idea to enable documentation agent.")


