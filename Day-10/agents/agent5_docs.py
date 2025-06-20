# agents/agent5_docs.py

import os
import tempfile
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# ✅ 1. Load the .env file and get the API key
load_dotenv()
api_key = ("AIzaSyCMhqcDUXJmBwjKFfU4OZmftbrLY-M1Od8")

# ✅ 2. Make sure API key exists
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file.")

# ✅ 3. Load the Gemini Flash model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0.3
)

# ✅ 4. Define Prompt Templates

# Case Booklet
case_booklet_prompt = PromptTemplate(
    input_variables=["project_description", "feedback", "iteration", "innovation", "pitch"],
    template="""
You are a documentation assistant for a student project.

Generate a case booklet in Markdown:

## 🎯 Purpose
Explain the idea, the user problem, and who benefits.

## 🔧 Process
Summarize feedback, development, and testing flow.

## 🧪 Testing Insights
Highlight what users liked/disliked.

## 🔁 Iteration Plan
List key improvements made after feedback.

## 🎤 Final Pitch
A concise summary of the product’s core message.

## 🚀 Innovation & Impact
Why is this idea unique? What potential does it have?
"""
)

# LinkedIn Caption
linkedin_prompt = PromptTemplate(
    input_variables=["project_description", "pitch", "innovation"],
    template="""
Write a LinkedIn-style caption (150–200 words) to promote this project. Highlight:
- What it solves
- What makes it unique
- Why people should check it out

Use a semi-professional and inspiring tone.
"""
)

# GitHub README
github_prompt = PromptTemplate(
    input_variables=["project_description", "feedback", "iteration", "innovation", "pitch"],
    template="""
Create a GitHub README in Markdown format.

# 📌 Overview
# 🚀 Features
# 🧪 Testing Summary
# 🔁 Iteration Plan
# 💡 Innovation
# 🔧 How to Use
"""
)

# ✅ 5. Define LangChain Chains
case_booklet_chain = LLMChain(llm=llm, prompt=case_booklet_prompt)
linkedin_chain = LLMChain(llm=llm, prompt=linkedin_prompt)
github_chain = LLMChain(llm=llm, prompt=github_prompt)

# ✅ 6. Define Agent 5 Runner
def run_documentation_agent(project_description, feedback, iteration, innovation, pitch):
    # Create a temporary folder to store output files
    temp_dir = tempfile.mkdtemp()

    # 1. Case Booklet Markdown
    case_md = case_booklet_chain.run(
        project_description=project_description,
        feedback=feedback,
        iteration=iteration,
        innovation=innovation,
        pitch=pitch
    )
    case_md_path = os.path.join(temp_dir, "case_booklet.md")
    with open(case_md_path, "w", encoding="utf-8") as f:
        f.write(case_md)

    # 2. LinkedIn Post
    linkedin_caption = linkedin_chain.run(
        project_description=project_description,
        pitch=pitch,
        innovation=innovation
    )
    linkedin_path = os.path.join(temp_dir, "linkedin_post.txt")
    with open(linkedin_path, "w", encoding="utf-8") as f:
        f.write(linkedin_caption)

    # 3. GitHub README
    readme_md = github_chain.run(
        project_description=project_description,
        feedback=feedback,
        iteration=iteration,
        innovation=innovation,
        pitch=pitch
    )
    readme_path = os.path.join(temp_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_md)

    # Return paths to the generated files
    return {
        "case_booklet_md": case_md_path,
        "linkedin_post": linkedin_path,
        "github_readme": readme_path
    }
