import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("best_salary_model.pkl")

# Page Config
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="wide"
)

# Header
st.markdown("""
<h1 style='text-align:center;'>
💰 AI Salary Predictor
</h1>

<h4 style='text-align:center;color:gray;'>
Discover your estimated market salary instantly
</h4>
""", unsafe_allow_html=True)

st.write("Predict your expected salary using Machine Learning")

# Layout - Two Columns
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Enter Your Name")
    age = st.slider("Age", 18, 65, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    education = st.selectbox("Education Level", ["Bachelor's", "Master's", 'PhD', "Bachelor's Degree", "Master's Degree",
 'High School'])
with col2:
    experience = st.slider("Years of Experience", 0, 35, 5)
    job_title = st.selectbox("Job Title",['Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate',
'Director', 'Marketing Analyst', 'Product Manager', 'Sales Manager',
'Marketing Coordinator', 'Senior Scientist', 'Software Developer',
'HR Manager', 'Financial Analyst', 'Project Manager', 'Customer Service Rep',
'Operations Manager', 'Marketing Manager', 'Senior Engineer',
'Data Entry Clerk', 'Sales Director', 'Business Analyst', 'VP of Operations',
'IT Support', 'Recruiter', 'Financial Manager', 'Social Media Specialist',
'Software Manager', 'Junior Developer', 'Senior Consultant',
'Product Designer', 'CEO', 'Accountant', 'Data Scientist',
'Marketing Specialist', 'Technical Writer', 'HR Generalist',
'Project Engineer', 'Customer Success Rep', 'Sales Executive', 'UX Designer',
'Operations Director', 'Network Engineer', 'Administrative Assistant',
'Strategy Consultant', 'Copywriter', 'Account Manager',
'Director of Marketing', 'Help Desk Analyst', 'Customer Service Manager',
'Business Intelligence Analyst', 'Event Coordinator', 'VP of Finance',
'Graphic Designer', 'UX Researcher', 'Social Media Manager',
'Director of Operations', 'Senior Data Scientist', 'Junior Accountant',
'Digital Marketing Manager', 'IT Manager',
'Customer Service Representative', 'Business Development Manager',
'Senior Financial Analyst', 'Web Developer', 'Research Director',
'Technical Support Specialist', 'Creative Director',
'Senior Software Engineer', 'Human Resources Director',
'Content Marketing Manager', 'Technical Recruiter', 'Sales Representative',
'Chief Technology Officer', 'Junior Designer', 'Financial Advisor',
'Junior Account Manager', 'Senior Project Manager', 'Principal Scientist',
'Supply Chain Manager', 'Senior Marketing Manager', 'Training Specialist',
'Research Scientist', 'Junior Software Developer',
'Public Relations Manager', 'Operations Analyst',
'Product Marketing Manager', 'Senior HR Manager', 'Junior Web Developer',
'Senior Project Coordinator', 'Chief Data Officer',
'Digital Content Producer', 'IT Support Specialist',
'Senior Marketing Analyst', 'Customer Success Manager',
'Senior Graphic Designer', 'Software Project Manager',
'Supply Chain Analyst', 'Senior Business Analyst',
'Junior Marketing Analyst', 'Office Manager', 'Principal Engineer',
'Junior HR Generalist', 'Senior Product Manager',
'Junior Operations Analyst', 'Senior HR Generalist',
'Sales Operations Manager', 'Senior Software Developer',
'Junior Web Designer', 'Senior Training Specialist',
'Senior Research Scientist', 'Junior Sales Representative',
'Junior Marketing Manager', 'Junior Data Analyst',
'Senior Product Marketing Manager', 'Junior Business Analyst',
'Senior Sales Manager', 'Junior Marketing Specialist',
'Junior Project Manager', 'Senior Accountant', 'Director of Sales',
'Junior Recruiter', 'Senior Business Development'])

# Predict Button
if st.button("🚀 Predict Salary"):

    # Prepare input sample
    sample = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education],
        "Job Title": [job_title],
        "Years of Experience": [experience]
    })

# Model prediction (This is your monthly salary from the dataset)
    with st.spinner("Analyzing profile..."):
        monthly = float(model.predict(sample))

    # Calculate yearly and daily salaries correctly
    prediction = monthly * 12
    daily = prediction / 365

    # Show results
    st.success(f"{name}, your predicted salary is ₹{prediction:,.0f}")

    # Display metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Annual Salary", f"₹{prediction:,.0f}")
    with col2:
        st.metric("📅 Monthly Salary", f"₹{monthly:,.0f}")
    with col3:
        st.metric("☀ Daily Salary", f"₹{daily:,.0f}")

    # Salary comparison chart
    comparison = pd.DataFrame({
        "Category": ["Average Salary", "Your Salary"],
        "Salary": [115327, prediction]
    })

    st.subheader("📊 Salary Comparison")
    st.bar_chart(comparison.set_index("Category"))

    # Progress bar
    salary_percent = min(prediction / 250000, 1.0)

    st.subheader("📈 Salary Level")
    st.progress(float(salary_percent))

    # Feedback message
    if prediction > 150000:
        st.success("🚀 Excellent earning potential!")
    elif prediction > 80000:
        st.info("📈 Strong salary range.")
    else:
        st.warning("📚 Upskilling could increase your salary.")

    st.balloons()  # Adds a celebratory effect
