# agents/agent4_pitch.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()
GEMINI_API_KEY = ("AIzaSyCMhqcDUXJmBwjKFfU4OZmftbrLY-M1Od8")

# ✅ Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.4
)

# 📝 Pitch Prompt Template
pitch_prompt = PromptTemplate(
    input_variables=["project_description", "iteration_plan", "innovation_scorecard"],
    template="""
You are a pitch coach assistant helping prepare a 3-minute pitch (~500 words) for a student startup project.

Generate a clear and engaging pitch script covering the following:
1. **Problem** - What real-world issue does this project solve?
2. **Solution** - What is the product/app and what does it do?
3. **Target Audience** - Who will benefit?
4. **UI/UX** - What is the interface like and how easy is it to use?
5. **User Testing Impact** - What did users say? What improvements were made?
6. **Innovation** - What makes this idea stand out?

Constraints:
- Format using clear section titles.
- Tone should be professional but adaptable to mentors, students, or early investors.
- Do not exceed ~500 words.

PROJECT IDEA:
{project_description}

ITERATION PLAN:
{iteration_plan}

INNOVATION SCORECARD:
{innovation_scorecard}
"""
)

# 🔁 Chain Initialization
pitch_chain = LLMChain(llm=llm, prompt=pitch_prompt)

# ✅ Agent 4: Pitch Generator Function
def run_pitch_agent(project_description: str, feedback: str, iteration_plan: str, innovation_scorecard: str) -> str:
    return pitch_chain.run(
        project_description=project_description,
        iteration_plan=iteration_plan,
        innovation_scorecard=innovation_scorecard
    )
