from pypdf import PdfReader
from langchain_core.prompts import PromptTemplate
from LangChainInput import Structured_model 

def analyze_resume(uploaded_file):
    # 1. Extract Text from PDF
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

    # 2. Resume Specific Prompt
    resume_template = """
    ### ROLE:
    You are a strict Senior Technical Recruiter scanning a resume.

    ### RESUME TEXT:
    {resume_text}

    ### INSTRUCTIONS:
    1. Analyze the projects and skills mentioned in the text.
    2. **Placement Check:** If the resume lacks good projects or modern tech stacks, mark 'False'.
    3. **Salary:** Estimate based on the skills found (Indian Market).
    4. **Tips:** Give 3 specific improvements for this resume (formatting, missing skills, or project complexity).
    """

    prompt = PromptTemplate(
        template=resume_template,
        input_variables=["resume_text"]
    )
    # chain is created by piping the prompt to the structured model
    chain = prompt | Structured_model
    
    result = chain.invoke({"resume_text": resume_text})

    return result