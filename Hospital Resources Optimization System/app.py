import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🏥 Hospital Resource Optimization System")

st.write("Predict Hospital Occupancy")

# Inputs
patients_admitted = st.number_input(
    "Patients Admitted",
    min_value=0
)

avg_stay = st.number_input(
    "Average Stay",
    min_value=0.0
)

avg_satisfaction = st.number_input(
    "Average Satisfaction",
    min_value=0.0,
    max_value=10.0
)

staff_count = st.number_input(
    "Staff Count",
    min_value=0
)

recommended_staff = st.number_input(
    "Recommended Staff",
    min_value=0
)

# Prediction
if st.button("Predict"):

    input_data = np.array([[
        patients_admitted,
        avg_stay,
        avg_satisfaction,
        staff_count,
        recommended_staff
    ]])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Occupancy: {prediction[0]:.2f}"
    )

    if prediction[0] < 10:
      st.success("✅ Low Occupancy")

    elif prediction[0] < 13:
      st.warning("⚠ Moderate Occupancy")

    else:
      st.error("🚨 High Occupancy Risk")
        
