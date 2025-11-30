import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# App UI
st.title("Air Quality Prediction App 🌍")
st.write("Enter environmental conditions to predict NO2 levels:")

# Input fields
T = st.number_input("Temperature (T)", value=20.0)
RH = st.number_input("Relative Humidity (RH)", value=50.0)
AH = st.number_input("Absolute Humidity (AH)", value=0.7)

# Predict Button
if st.button("Predict"):
    # Convert inputs to numpy array
    input_data = np.array([[T, RH, AH]])

    # Run prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted NO2 Level: {prediction[0]:.2f}")

