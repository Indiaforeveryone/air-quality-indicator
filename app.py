import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("Air Quality Predictor (NO2 Level)")
st.subheader("Enter environmental conditions:")

# Input form
temperature = st.number_input("Temperature (T)", min_value=-50.0, max_value=50.0, step=0.1)
humidity = st.number_input("Relative Humidity (RH)", min_value=0.0, max_value=100.0, step=0.1)
absolute_humidity = st.number_input("Absolute Humidity (AH)", min_value=0.0, max_value=10.0, step=0.01)

if st.button("Predict NO2 Level"):
    try:
        # Prepare input in the same shape model was trained on
        features = np.array([[temperature, humidity, absolute_humidity]])

        prediction = model.predict(features)[0]
        st.success(f"Predicted NO₂ Level: {prediction:.2f} µg/m³")

    except Exception as e:
        st.error(f"Error: {e}")
