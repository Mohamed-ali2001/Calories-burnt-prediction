import numpy as np
import pickle
import streamlit as st

# Load the trained model from file
loaded_model = pickle.load(open('trained_best_model.sav','rb'))

# Creating a predictive function
def calories_burnt_prediction(inputdata):
    # Convert input data to numpy array
    inputdata_as_numpy_array = np.asarray(inputdata)
    # Reshape for prediction (single sample)
    input_data_reshaped = inputdata_as_numpy_array.reshape(1,-1)
    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]


def main():
    st.title("Calories burnt prediction")
    # User input fields for model features
    Gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    Age = st.number_input("Age", min_value=0)
    Height = st.number_input("Height (cm)", min_value=0.0)
    Weight = st.number_input("Weight (kg)", min_value=0.0)
    Duration = st.number_input("Duration (min)", min_value=0.0)
    Heart_Rate = st.number_input("Heart Rate", min_value=0)
    Body_Temp = st.number_input("Body Temperature", min_value=0.0)

    # Collect all inputs for prediction
    inputdata = [Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]
    prediction = 0
    # Run prediction when button is clicked
    if st.button('Calories burnt prediction result'):
        prediction = calories_burnt_prediction(inputdata)
    # Display prediction result
    st.success(prediction)


if __name__ == '__main__':
    main()