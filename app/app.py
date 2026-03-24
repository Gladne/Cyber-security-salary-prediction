import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

st.set_page_config(
    page_title="Cybersecurity Salary Predictor",
    page_icon="🔒",
    layout="centered"
)

# Load models
model = joblib.load(BASE_DIR / "models/xgb_model.pkl")
model_columns = joblib.load(BASE_DIR / "models/model_columns.pkl")


# Manual mappings
experience_map = {'EN': 0, 'MI': 1, 'SE': 2, 'EX': 3}
employment_map = {'CT': 0, 'FL': 1, 'FT': 2, 'PT': 3}
company_size_map = {'L': 0, 'M': 1, 'S': 2}

job_category_list = [
    'Analyst', 'Architect', 'Consultant', 'Engineer',
    'Executive', 'Manager', 'Offensive Security',
    'Researcher', 'Specialist', 'Other'
]
job_category_map = {cat: i for i, cat in enumerate(sorted(job_category_list))}


def jobcategories(title):
    title = title.lower()

    if "engineer" in title:
        return "Engineer"
    elif "specialist" in title:
        return "Specialist"
    elif any(x in title for x in ["head", "director", "chief"]):
        return "Executive"
    elif "manager" in title:
        return "Manager"
    elif "consultant" in title:
        return "Consultant"
    elif "analyst" in title:
        return "Analyst"
    elif "architect" in title:
        return "Architect"
    elif "research" in title:
        return "Researcher"
    elif any(x in title for x in ["penetration", "ethical hacker", "offensive"]):
        return "Offensive Security"
    else:
        return "Other"


st.title("Cyber Security Salary Prediction")

job_titles = [
    'Information Security Officer', 'Security Engineer',
    'Penetration Tester', 'Cyber Security Analyst',
    'Cloud Security Engineer', 'Security Consultant',
    'SOC Analyst', 'Security Architect',
    'Chief Information Security Officer'
]

# Input form
with st.form("Prediction form"):

    with st.expander("ℹ️ See abbreviation meanings"):
        st.markdown("""
                    **Experience Level**
                    - EN: Entry level  
                    - MI: Mid level  
                    - SE: Senior level 
                    - EX: Executive level  

                    **Employment Type**
                    - FT: Full Time  
                    - PT: Part Time  
                    - CT: Contract 
                    - FL: Freelance  

                    **Company Size**
                    - S: Small (1–50 employees) 
                    - M: Medium (50–250 employees)
                    - L: Large (250+ employees)  
                    """)

    col1, col2 = st.columns(2)

    with col1:
        job_title = st.selectbox("Job Title", job_titles)
        experience_level = st.selectbox("Experience Level", ['EN', 'MI', 'SE', 'EX'])
        employment_type = st.selectbox("Employment Type", ['FT', 'PT', 'CT', 'FL'])
        remote_ratio = st.slider("Remote Ratio (%)", 0, 100, 50)

    with col2:    
        company_size = st.selectbox("Company Size", ['S', 'M', 'L'])
        employee_residence = st.selectbox(
            "Employee Residence",
            ['Asia', 'Europe', 'North America', 'South America', 'Oceania']
            )
        company_location = st.selectbox(
            "Company Location",
            ['Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Other']
            )
    
    submitted = st.form_submit_button("Predict Salary")       

# Prediction
if submitted:
    job_category = jobcategories(job_title)

    # Base numeric features
    input_dict = {
        'experience_level': experience_map[experience_level],
        'employment_type': employment_map[employment_type],
        'remote_ratio': remote_ratio,
        'company_size': company_size_map[company_size],
        'job_category': job_category_map.get(job_category, 0)
    }

    # Manual one-hot encoding
    regions = ['Asia', 'Europe', 'North America', 'South America', 'Oceania']

    for region in regions:
        input_dict[f'employee_residence_{region}'] = 1 if employee_residence == region else 0

    company_regions = ['Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Other']

    for region in company_regions:
        input_dict[f'company_location_{region}'] = 1 if company_location == region else 0

    input_data = pd.DataFrame([input_dict])

    # Match training columns
    expected_columns = model.get_booster().feature_names

    input_data = input_data.reindex(columns=expected_columns, fill_value=0)

    # Predict
    prediction_log = model.predict(input_data)
    prediction = np.expm1(prediction_log)

    st.success(f"Estimated Salary: ${prediction[0]:,.2f}")