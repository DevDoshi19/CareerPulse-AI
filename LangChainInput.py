from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

try:
    # Try to grab it from Streamlit Secrets (Works on Cloud)
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    # If secrets file is missing (Works on Local Laptop), use .env
    api_key = os.getenv("GOOGLE_API_KEY")

# pydentic model for structured output
class chatInputValidation(BaseModel):
    is_placed : bool = Field(description="Whether the candidate is likely to get placed (True/False)")
    role : str = Field(description="The most suitable job role for this candidate (e.g.,AI Enginneer ,ML Enginner ,Genai Enginner ,Product Manager)")
    salary : str = Field(description="Estimated salary range based on current market (e.g., '6-8 LPA')")
    tips : List[str] = Field(description="A list of 3 specific, actionable tips to improve chances")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6,api_key=api_key)
Structured_model = model.with_structured_output(chatInputValidation)

# function to analyze manual input
def analyze_manual_input(cgpa, exp_level, skills, project):

    manual_template = """
    ### ROLE:
    You are a Senior Technical Recruiter and Career Coach with 20+ years of experience hiring for top tech companies (FAANG, Startups, and MNCs). 
    You have deep knowledge of the current job market in AI, Data Science, and Software Engineering. 
    You are brutally honest but constructive.

    ### CANDIDATE PROFILE:
    - **Education/CGPA:** {cgpa}
    - **Experience Level:** {experience_level} (Fresher/Experienced)
    - **Technical Stack:** {skills}
    - **Showcase Project:** {project_description}

    ### TASK:
    Analyze the candidate's profile against current industry standards. 
    1. **Placement Check:** Be strict. If the project is too simple , mark them as 'False'.
    2. **Salary Estimation:** Provide a realistic package in **LPA** (Lakhs Per Annum). Do not give inflated US-standard salaries. 
    3. **Feedback:** Provide exactly **3 tips**.
    - CONSTRAINT: Keep each tip extremely short (1 sentence maximum).
    - Focus on adding complexity to projects or learning deployment (Docker/AWS).
    """

    prompt = PromptTemplate(
        template=manual_template,
        input_variables=["cgpa", "experience_level", "skills", "project_description"],
    )

    chain = prompt | Structured_model

    return chain.invoke({
        "cgpa": cgpa,
        "experience_level": exp_level,
        "skills": skills,
        "project_description": project
    })