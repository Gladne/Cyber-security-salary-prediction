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
- RMSE: 0.313
- MAE: 0.071
- R² Score: 0.786

### Gradient Boosting Regressor
- RMSE: 0.263
- MAE: 0.056
- R² Score: 0.849

### XGBoost Regressor
- RMSE: 0.351
- MAE: 0.171
- R² Score: 0.732

### Hyperparameter Tuning
Hyperparameter tuning was applied to improve the Gradient Boosting model using RandomizedSearchCV. </br>
__Best Parameters:__
- n_estimators: 400
- learning_rate: 0.05
- max_depth: 3
- min_samples_split: 5
- min_samples_leaf: 1

__Tuned Model Performance:__
- RMSE: 0.261
- MAE: 0.055

The tuned Gradient Boosting model achieved the best performance among all models.

# Final Conclusion

The Gradient Boosting Regressor demonstrated the strongest predictive performance with the lowest error and highest R² score. 
Hyperparameter tuning further improved the model, confirming that optimized parameters enhance prediction accuracy. 
Therefore, the tuned Gradient Boosting model was selected as the final model for salary prediction.

### Technologies Used
Python, Pandas, NumPy, Matplotlib / Seaborn, Scikit-learn, XGBoost

## How to Run the Project
git clone https://github.com/your-username/cybersecurity-salary-prediction.git </br>
pip install pandas numpy matplotlib seaborn scikit-learn xgboost </br>
jupyter notebook
