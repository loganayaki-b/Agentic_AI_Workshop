# 🧠 AI-Powered Job Role Recommender using Multi-Agent LLMs and RAG

## 📌 Problem Statement  
Candidates often struggle to align their resumes or career intent with the right job roles. HRs may also misinterpret candidate aspirations, leading to mismatches and higher attrition.

## 🎯 Project Goal  
To create an AI-powered system that takes user-uploaded resumes or career intent PDFs and automatically:

- Understands the candidate's intent
- Maps skills and aspirations
- Recommends suitable job roles using Retrieval-Augmented Generation (RAG)
- Predicts retention risk based on alignment between skills and aspirations

## 🧩 Multi-Agent Architecture  
This app uses **LangChain AgentExecutor** with **Gemini 2.0 Flash** models and consists of the following four agents:

1. **Career Intent Extraction Agent**  
   → Extracts and summarizes the candidate's career goals from the uploaded PDF.

2. **Skill & Aspiration Mapping Agent**  
   → Matches user skills and aspirations using the extracted intent and full resume.

3. **Role Matching Agent (RAG-based)**  
   → Uses embedded job role documents (PDF) to retrieve relevant roles and recommend the best matches.

4. **Retention Risk Analyzer Agent**  
   → Evaluates how well the candidate aligns with the recommended roles to predict potential job retention risk.

## 💡 How It Works  
- The user uploads a PDF (e.g., resume or career statement).
- Agents work sequentially to process and analyze content.
- Final output includes:
  - Career intent summary
  - Skill mapping
  - RAG-based job recommendations
  - Retention risk level

## 🖥️ Streamlit UI Flow

```
Upload PDF --> Career Intent --> Skills & Aspirations --> Role Recommendation (RAG) --> Risk Prediction
```

## 🛠️ Tech Stack

| Layer             | Technology                              |
|------------------|------------------------------------------|
| UI               | Streamlit                                |
| Framework        | LangChain                                |
| Model            | Gemini 2.0 Flash                         |
| Vector DB        | FAISS (using local PDF chunks)           |
| Document Parsing | PyPDF / pdfplumber                       |
| Environment      | Python 3.10+ in VS Code                  |

## 📁 Folder Structure

```
job_role_recommender/
│
├── main.py                        # Streamlit app
├── .env                           # Environment variables (API keys)
├── requirements.txt               # Python dependencies
│
├── utils/                         # Utility agents and modules
│   ├── pdf_reader.py              # Extracts text from PDF
│   ├── intent_agent.py            # Career Intent Agent
│   ├── skill_agent.py             # Skill Mapping Agent
│   ├── rag_agent.py               # Role Matcher (RAG)
│   ├── risk_agent.py              # Retention Risk Agent
│
├── data/
│   └── job_roles/                 # Folder for role PDFs for RAG
│       ├── software_engineer.pdf
│       ├── data_analyst.pdf
│       └── ...
```

## ⚙️ How to Run the App

### ✅ 1. Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ 2. Setup your `.env` file

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### ✅ 3. Add job role PDFs for RAG

Place role descriptions (as PDFs) inside the `data/job_roles/` folder.

### ✅ 4. Run the Streamlit app

```bash
streamlit run main.py
```

## 📌 Example Output

- **Career Intent**: “I want to become a Data Scientist who solves real-world business problems using AI.”
- **Skill Map**: “You have experience with Python, SQL, and ML tools. You aspire toward analytics-driven roles.”
- **Job Recommendations**: Data Analyst, AI Research Intern, ML Engineer
- **Retention Risk**: “Low – Strong alignment between goals and recommended roles.”

## 🧪 Sample PDF Test Inputs  
Place your resume or intent documents in `.pdf` format for testing.  
Use simple intent like:  
> “I am passionate about cloud computing and backend development using Python.”
