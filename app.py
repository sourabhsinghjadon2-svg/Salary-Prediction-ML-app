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
    job_title = st.text_input("Job Title", "Data Scientist")

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

    # Model prediction
    with st.spinner("Analyzing profile..."):
        prediction = model.predict(sample)[0]

    # Calculate monthly and daily salaries
    monthly = prediction / 12
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
