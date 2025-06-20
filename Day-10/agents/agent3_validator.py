# agent3_validator.py

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from rag.retriever import retrieve_from_pdf  # Custom RAG logic

# Load environment variables
load_dotenv()
api_key = ("AIzaSyBiHRgezbsvPKHUZaRoj-WCBLbcWRls0Qw")

# ✅ Gemini Flash Model Loader
def get_gemini_llm():
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found in .env file.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0.3
    )

# ✅ Agent 3: Innovation Validator
def run_validator_agent(project_description: str, uploaded_pdf_file: str) -> str:
    if not project_description.strip():
        return "❌ Error: Project description cannot be empty."
    if not uploaded_pdf_file:
        return "❌ Error: PDF file path cannot be empty."

    llm = get_gemini_llm()

    # Retrieve context from RAG
    try:
        matches = retrieve_from_pdf(project_description, uploaded_pdf_file)
        matched_context = "\n\n".join(matches) if matches else "No matches found in the provided PDF."
    except Exception as e:
        matched_context = f"Error retrieving matches: {str(e)}"

    # Structured Prompt
    prompt = f"""
You are an innovation validator for AI startup ideas. Given a product idea and context from a PDF, produce a scorecard in **strict markdown format** with the exact structure below.

---

📌 **Idea Summary**:
- {project_description}

📈 **1. Matched Startups**:
- List 2–3 unicorns from the context below and briefly explain how they relate.
- If no matches are found, state: "No relevant startups found in the provided context."
- Context: {matched_context}

💡 **2. Uniqueness**:
- State whether the idea is original (High), moderately unique (Moderate), or common (Low).
- Explain what makes it different or similar to existing solutions.

🔁 **3. Repeat Usage Potential**:
- Specify if users would return daily, weekly, or monthly.
- Provide a brief reason why.

🛠️ **4. Improvements**:
- Suggest 2–3 specific improvements to enhance the idea.

🚀 **5. Pivot Suggestions**:
- Recommend 1–2 alternative markets, audiences, or use cases.

---

**RULES**:
- Use only markdown format with the exact headings and emojis (📌, 📈, 💡, 🔁, 🛠️, 🚀).
- Do not add any extra text, summaries, or paragraphs outside the structure.
- Keep responses concise and relevant to the idea and context.
"""

    # Generate scorecard
    try:
        return llm.invoke(prompt).content
    except Exception as e:
        return f"❌ Error generating scorecard: {str(e)}"
