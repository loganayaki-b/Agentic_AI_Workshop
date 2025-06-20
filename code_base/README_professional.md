
# Agentic Testing Assistant

Agentic Testing Assistant is a multi-agent Streamlit application built using LangChain, Gemini Flash, and Retrieval-Augmented Generation (RAG). It guides students, product designers, and founders through a complete product testing and validation pipeline with five intelligent agents.

---

## Overview

This system is designed to help users analyze feedback, plan improvements, validate innovation, generate startup pitches, and prepare launch-ready documentation.

---

## Agents Overview

### Agent 1: Feedback Analysis Agent
- Extracts key usability issues, user emotions, and improvement suggestions from uploaded user testing notes or interview transcripts.
- Helps identify pain points and user sentiments during product testing.

### Agent 2: Iteration Planning Agent
- Generates a structured iteration roadmap based on insights from Agent 1.
- Suggests enhancements, redesigns, or removals to align with user needs.

### Agent 3: Innovation Validator Agent
- Uses RAG with a unicorn startup PDF knowledge base.
- Benchmarks the user’s idea against successful startups and validates its uniqueness, usage potential, and improvement scope.

### Agent 4: Pitch Generator Agent
- Crafts a clear and compelling startup pitch.
- Integrates validated insights and structured iterations to produce a market-facing summary for presentations.

### Agent 5: Documentation & Branding Agent
- Creates a case booklet (Markdown), a LinkedIn announcement draft, and a GitHub README.
- Consolidates all outputs from Agents 1–4 to generate launch-ready assets.

---

## Technologies Used

- LangChain with AgentExecutor
- Gemini 1.5 / 2.0 Flash via Google Generative AI
- Streamlit for interactive UI
- PyPDF2 and FAISS for RAG PDF parsing
- Markdown and PDFKit for document generation

---

## Project Structure

```
agentic_testing_assistant/
├── main.py
├── agents/
│   ├── agent1_feedback.py
│   ├── agent2_iteration.py
│   ├── agent3_validator.py
│   ├── agent4_pitch.py
│   └── agent5_docs.py
├── rag/
│   ├── retriever.py
│   └── vectorstore.py
├── utils/
│   ├── file_handler.py
│   └── pdf_reader.py
├── startup data/
│   └── unicorns_5_domains.pdf
└── .env
```

---

## Setup Instructions

1. Clone this repository in Visual Studio Code.
2. Create a `.venv` and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and set your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run main.py
   ```

---

## Output Files

Upon completing all 5 agents, you can download:
- `case_booklet.md`: Summarized journey from feedback to final pitch
- `linkedin_post.txt`: Draft announcement for LinkedIn
- `README.md`: Auto-generated GitHub README

---

## License

This project is developed for educational and prototyping purposes only.


Agent Workflow Overview:-

The agents work sequentially to simulate a complete product testing and launch validation cycle:

Agent 1 – Feedback Analysis
Takes in user testing notes or interview transcripts and extracts key usability issues, emotional reactions, and grouped user suggestions.

Agent 2 – Iteration Planning
Uses Agent 1's output to create a structured iteration roadmap, suggesting which features to enhance, redesign, or remove.

Agent 3 – Innovation Validator
Compares the final product idea with real-world unicorn startups using a RAG system to check for originality, improvement potential, and repeat usage potential.

Agent 4 – Pitch Generator
Crafts a concise, compelling startup pitch that integrates insights from feedback, planning, and innovation benchmarking.

Agent 5 – Documentation & Branding
Generates launch-ready assets including a case booklet, GitHub README, and a LinkedIn post, summarizing the full journey from idea to pitch.
