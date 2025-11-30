import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("Air Quality Prediction 🚦")
st.write("Enter environmental values to predict NO2 levels:")

T = st.number_input("Temperature (°C)", min_value=-20.0, max_value=60.0, value=20.0)
RH = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
AH = st.number_input("Absolute Humidity", min_value=0.0, max_value=5.0, value=1.0)

input_data = np.array([[T, RH, AH]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted NO2 Level: {prediction[0]:.2f}")