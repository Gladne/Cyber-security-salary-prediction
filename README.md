# Cyber Security Salary Prediction

A machine learning web app that predicts cybersecurity salaries based on job attributes such as experience level, role, and location.

**Live Demo:**
https://cyber-security-salary-prediction-version-1.streamlit.app/

**Repository:**
https://github.com/Gladne/Cyber-security-salary-prediction.git

---
## Project Overview
This project applies machine learning to estimate salaries in the cybersecurity field. 
It combines data preprocessing, feature engineering, and an XGBoost model deployed through a Streamlit interface.

---

## Key Features

* Interactive web app built with Streamlit
* Real-time salary prediction
* Custom job title categorization
* Manual feature encoding for model consistency
* Clean and user-friendly UI

---

## Model Highlights

* **Algorithm:** XGBoost Regressor
* **Target Transformation:** Log transformation (improves accuracy)
* **Features Used:**

  * Experience level
  * Employment type
  * Remote work ratio
  * Company size
  * Job category
  * Geographic location

---

## Tech Stack

* Python
* Streamlit
* Pandas & NumPy
* Scikit-learn
* XGBoost
* Joblib

---

## Run Locally

```bash
git clone https://github.com/Gladne/Cyber-security-salary-prediction.git
cd Cyber-security-salary-prediction
pip install -r requirements.txt
streamlit run app.py
```
---

## How It Works

1. User inputs job details
2. Inputs are encoded and aligned with training features
3. Model predicts log salary
4. Final salary is converted back and displayed
