import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.joblib")

# App UI
st.title("Air Quality Prediction App 🌍")

T = st.number_input("Temperature (T)", value=20.0)
RH = st.number_input("Relative Humidity (RH)", value=50.0)
AH = st.number_input("Absolute Humidity (AH)", value=0.7)

if st.button("Predict"):
    input_data = np.array([[T, RH, AH]])
    prediction = model.predict(input_data)
    st.success(f"Predicted NO2 Level: {prediction[0]:.2f}")

