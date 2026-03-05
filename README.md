# Cybersecurity Labor Market Analysis & Salary Prediction

# Project Overview
This project analyzes the cybersecurity labor market and builds machine learning models to predict salaries based on job-related features.
The objective is to explore trends in the cybersecurity workforce and develop a predictive model with strong performance and low error.

# The project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Model training and evaluation
- Hyperparameter tuning
- Model comparison and final selection

# Dataset
The [Cyber_salaries](https://www.kaggle.com/datasets/whenamancodes/infoseccyber-security-salaries/data) dataset contains cybersecurity job and salary information, including:
- Job role / title
- Experience level
- Company size
- Employment type
- Work setting / location
- Salary (target variable)

# Exploratory Data Analysis
EDA was performed to understand:
- Salary distribution across experience levels
- Job role demand in the cybersecurity market
- Impact of company size and employment type on salary
- Feature correlations and data patterns

# Machine Learning Models
The following regression models were trained and evaluated:
### Random Forest Regressor
- RMSE: 41323.38
- MAE: 30934.92
- R² Score: 0.349

### Gradient Boosting Regressor
- RMSE: 39077.72
- MAE: 29125.05
- R² Score: 0.418

### XGBoost Regressor
- RMSE: 37800.98
- MAE:  28230.66
- R² Score:  0.455

### Hyperparameter Tuning
Hyperparameter tuning was applied to improve the Gradient Boosting model using RandomizedSearchCV. </br>
__Best Parameters:__
- n_estimators: 400
- learning_rate: 0.01
- max_depth: 4
- min_child_weight: 3
- colsample_bytree: 0.85

The tuned XGBoost model performed better than other models ('Random Forest' and 'Gradient Boosting').

### Technologies Used
Python, Pandas, NumPy, Matplotlib / Seaborn, Scikit-learn, XGBoost

## How to test the App
https://cyber-security-salary-prediction-version-1.streamlit.app/

## How to Run the Project
git clone https://github.com/your-username/cybersecurity-salary-prediction.git </br>
pip install pandas numpy matplotlib seaborn scikit-learn xgboost </br>
jupyter notebook
