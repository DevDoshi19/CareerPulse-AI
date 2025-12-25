<h1 align="left">🚀 CareerPulse AI – Placement Predictor</h1>

<h3 align="left">
An AI-powered placement analysis tool built using <strong>Streamlit</strong> and <strong>LangChain</strong>,  
designed to evaluate a candidate’s profile and predict <strong>job readiness, role, salary range, and improvement tips</strong>.
</h3>

<br/>

<div align="center">
  <img height="200" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" />
</div>

---

## 🧠 What is CareerPulse AI?

**CareerPulse AI** is an intelligent career analysis application that simulates how a **senior technical recruiter** evaluates candidates.

Based on either:
- 📝 **Manual profile input**, or  
- 📂 **Uploaded resume (PDF)**  

the system predicts:
- ✅ Placement readiness (Hire / Needs Improvement)
- 🎯 Best-suited job role
- 💰 Estimated salary range (Indian market)
- 💡 3 actionable improvement tips

This project focuses on **realistic hiring standards**, not inflated or generic AI responses.

---

## 🎯 Key Features

- 🧩 **Dual Input Modes**
  - Manual profile form
  - Resume PDF upload

- 🧠 **LLM-based Evaluation**
  - Uses Gemini via LangChain
  - Structured, reliable output using Pydantic

- 📊 **Actionable Results**
  - Placement verdict
  - Role recommendation
  - Salary estimation (LPA)
  - Clear, concise improvement tips

- ⚡ **Production-Ready UX**
  - Loading spinners
  - Graceful error handling
  - API rate-limit protection

---

<div align="center">
  <img height="200" src="https://media.giphy.com/media/jBOOXxSJfG8kqMxT11/giphy.gif" />
</div>

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM:** Google Gemini (via LangChain)  
- **Framework:** LangChain (Prompt → Model → Structured Output)  
- **Validation:** Pydantic  
- **PDF Parsing:** PyPDF  
- **Secrets Management:** `.env` + Streamlit Secrets  

---

## 🧩 How It Works (High Level)

```

User Input (Form / Resume)
↓
Prompt Engineering (Recruiter Persona)
↓
Gemini LLM (Structured Output)
↓
Placement Verdict + Salary + Role + Tips

```

The model is instructed to behave like a **strict senior recruiter**, ensuring realistic outputs.

---

## 🧠 Core Logic Overview

### 1️⃣ Manual Input Analysis
- CGPA
- Experience level
- Skills
- Best project

The model evaluates:
- Project complexity
- Skill relevance
- Market readiness

---

### 2️⃣ Resume PDF Analysis
- Extracts text using `PdfReader`
- Analyzes skills, projects, and resume quality
- Flags weak resumes honestly

---

### 3️⃣ Structured Output (No Hallucinations)

The LLM output is enforced using **Pydantic schema**, ensuring:
- Boolean placement decision
- Clean role name
- Realistic salary range
- Exactly 3 concise tips

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/CareerPulse-AI.git
cd CareerPulse-AI
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Create `.env` File

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

⚠️ Never commit `.env` to GitHub.

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 What I Learned from This Project

* Prompt engineering with **real-world personas**
* Using **LangChain structured output** to avoid messy responses
* Handling **API rate limits** gracefully
* Building clean separation between:

  * UI logic
  * LLM logic
  * Resume parsing
* Designing AI apps that feel **useful, not gimmicky**

---

## 🚀 Future Improvements

* Resume scoring breakdown
* Skill-gap visualization
* Persistent user sessions
* Deployment on Streamlit Cloud / AWS
* RAG-based job market insights

---

## 👨‍💻 Author

**Dev Doshi**
AI / ML | LangChain | Generative AI | Problem Solving

---

## 🔗 Let’s Connect

<div align="left">
  <a href="https://www.linkedin.com/in/dev-doshi-8360a727b" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg"
         width="52" height="40" />
  </a>
</div>

---

⭐ If you found this project interesting, consider starring the repository.


Just say the word 💪




