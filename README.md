# Calories Burnt Prediction Web App

## Project Overview
This project predicts the number of calories burnt during exercise using biometric and activity features. It leverages machine learning models trained on the Kaggle "Calories Burnt Prediction" dataset and provides an interactive web app for predictions.

## Features
- Data loading, cleaning, and exploratory analysis
- Model training and evaluation (Linear Regression, Random Forest, SVR, KNN, Gradient Boosting)
- Model comparison and selection
- Explainability using feature importance and SHAP values
- Streamlit web app for user-friendly predictions

## Dataset
- `exercise.csv`: Contains biometric and activity features
- `calories.csv`: Contains target variable (calories burnt)

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train models and save the best model as `trained_best_model.sav` (see notebook for details).
3. Launch the Streamlit app:
   ```bash
   streamlit run Calories_burnt_prediction_web_app.py
   ```

## Usage
- Enter exercise and biometric details in the web app to get a calories burnt prediction.
- The app uses the best-performing model (Gradient Boosting or Random Forest) for predictions.

## Explainability
- Feature importance and SHAP values are used to interpret model predictions and understand key drivers of calorie burn.

## Files
- `Calories_burnt_prediction.ipynb`: Main notebook with data analysis, modeling, and explainability
- `Calories_burnt_prediction_web_app.py`: Streamlit app for predictions
- `requirements.txt`: List of required Python libraries
- `trained_best_model.sav`: Saved best model for deployment


