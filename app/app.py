import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load models, columns and encoders
model = joblib.load("../models/xgb_model.pkl")
features = joblib.load("../models/model_columns.pkl")
exp_encoder = joblib.load("../models/experience_encoder.pkl")
emptype_encoder = joblib.load("../models/emptype_encoder.pkl")
compsize_encoder = joblib.load("../models/compsize_encoder.pkl")
job_title_encoder = joblib.load("../models/job_title_encoder.pkl")

st.set_page_config(page_title="Cyber Salary Predictor", layout="centered")
st.title("Cyber Security Salary Prediction")
st.write("Fill in the details below to predict the estimated cybersecurity salary")

# Input form
with st.form("Prediction form"):
    #st.subheader("Enter Employee Data")

    col1, col2 = st.columns(2)

    with col1:
        # job title column
        job_title = st.text_input("Job title")

        # experience level column
        exp_map = {
            "Entry Level": "EN",
            "Mid Level": "MI",
            "Senior Level": "SE",
            "Executive Level": "EX"
        }

        exp_display = list(exp_map.keys())
        explevel_display = st.selectbox("Experience Level", exp_display)
        # Convert to model value
        experience_level = exp_map[explevel_display]

        # employment type column
        emptype_map = {
            "Full Time": "FT",
            "Part Time": "PT",
            "Contract Time": "CT",
            "Freelance": "FL"
        }

        emptype_display = list(emptype_map.keys())
        employment_type_display = st.selectbox("Employment Type",emptype_display)
        employment_type = emptype_map[employment_type_display]

        # company size column
        compsize_map = {
            "Small Company": "S",
            "Medium Company": "M",
            "Large Company": "L"
        }

        compsize_display = list(compsize_map.keys())
        company_size_display = st.selectbox("Company Size", compsize_display)
        company_size = compsize_map[company_size_display]

    with col2:
        # employee residence
        residence_map = {
            "North America": "employee_residence_North America",
            "Europe": "employee_residence_Europe",
            "Asia": "employee_residence_Asia",
            "Oceania": "employee_residence_Oceania",
            "South America": "employee_residence_South America",
            "Africa": "employee_residence_Africa"
        }

        residence_display = list(residence_map.keys())
        employee_residence_display = st.selectbox("Employee Residence", residence_display)
        employee_residence = residence_map[employee_residence_display]

        # company location column
        complocation_map = {
            "North America": "company_location_North America",
            "Europe": "company_location_Europe",
            "Asia": "company_location_Asia",
            "Oceania": "company_location_Oceania",
            "South America": "company_location_South America",
            "Africa": "company_location_Africa",
            "Other": "company_location_Other"
        }

        complocation_display = list(complocation_map.keys())
        company_location_display = st.selectbox("Company Location", complocation_display)
        company_location = complocation_map[company_location_display]

        # remote ratio column
        remote_ratio = st.slider("Remote ratio (%)", 0, 100, 50)

    submitted = st.form_submit_button("Predict Salary")    

# Safe Encoder
def safe_encoder(encoder, value):
   if value in encoder.classes_:
       return encoder.transform([value])[0]
   return -1 # returns -1 if the value is not seen during training

# Prediction
if submitted:
    row = {
        "experience_level": exp_encoder.transform([[experience_level]])[0][0],
        "employment_type": emptype_encoder.transform([[employment_type]])[0][0],
        "job_title": safe_encoder(job_title_encoder, job_title),
        "remote_ratio":remote_ratio,
        "company_size":compsize_encoder.transform([[company_size]])[0][0],
    }

    input_data = pd.DataFrame([row])

    full_input = pd.DataFrame(columns=features)
    full_input.loc[0] = 0

    for col in input_data.columns:
        if col in full_input.columns:
            full_input[col] = input_data[col].iloc[0]

    # activate onehot columns
    def activate(col):
        if col in full_input.columns:
            full_input[col] = 1

    activate(f"employee_residence_{employee_residence}")
    activate(f"company_location_{company_location}")

    full_input = full_input.reindex(columns=features, fill_value=0)

    # Predict
    prediction_log = model.predict(full_input)
    prediction = np.expm1(prediction_log)

    st.success(f"Estimated Salary: ${prediction[0]:,.2f}")
