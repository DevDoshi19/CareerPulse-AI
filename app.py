import streamlit as st
from LangChainInput import analyze_manual_input
from LangChainResume import analyze_resume
from google.api_core.exceptions import ResourceExhausted

st.set_page_config(page_title="CareerPulse AI", page_icon="🚀")

st.title("🚀 CareerPulse: AI Placement Predictor")
st.subheader("Will you get hired? Let's check.")

input_mode = st.radio(
    "Choose Input Method:",
    ["📝 Fill Manual Details", "📂 Upload Resume (PDF)"],
    horizontal=True
)

result = None 

if input_mode == "📝 Fill Manual Details":
    with st.form("manual_form"):
        cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
        exp_level = st.selectbox("Experience Level", ["Fresher", "0-1 Year", "1-3 Years","3+ Years"])
        skills = st.text_area("Skills (e.g., Python, React, AWS)")
        project = st.text_area("Describe your Best Project")
        
        submitted = st.form_submit_button("Analyze Profile")
        
        if submitted:
            with st.spinner("Consulting the Hiring Manager..."):
                try :
                    result = analyze_manual_input(cgpa, exp_level, skills, project)
                except ResourceExhausted:
                    # This runs ONLY if the limit is reached
                    st.error("⏳ The AI is currently overwhelmed with requests. Please wait 1 minute and try again.")
        
                except Exception as e:
                    # This runs for any other crash
                    st.error(f"An unexpected error occurred: {e}")
        
elif input_mode == "📂 Upload Resume (PDF)":
    uploaded_file = st.file_uploader("Upload your Resume", type="pdf")
    
    if uploaded_file is not None:
        if st.button("Analyze Resume"):
            with st.spinner("Scanning Resume..."):
                try :
                    result = analyze_resume(uploaded_file)
                except ResourceExhausted:
                    # This runs ONLY if the limit is reached
                    st.error("⏳ The AI is currently overwhelmed with requests. Please wait 1 minute and try again.")
                
                except Exception as e:
                    # This runs for any other crash
                    st.error(f"An unexpected error occurred: {e}")


# --- DISPLAY RESULTS (Common for both) ---
if result:
    st.divider()
    
    # 1. Top Section: Verdict
    if result.is_placed:
        st.success(f"✅ **You are Job Ready!** (Likely Role: {result.role})")
    else:
        st.error(f"⚠️ **Needs Improvement** (Target Role: {result.role})")

    # 2. Metrics Column
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Estimated Salary (LPA)", value=result.salary)
    with col2:
        st.metric(label="Market Status", value="Hirable" if result.is_placed else "Upskill Needed")

    # 3. Tips Section
    st.markdown("### 💡 Professional Advice:")
    for tip in result.tips:
        st.info(tip)