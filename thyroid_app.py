import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("thyroid_model.pkl")

st.title("🩺 Thyroid Disease Predictor")

st.markdown("### Enter your thyroid test values:")
tsh = st.number_input("TSH (mIU/L)", min_value=0.0, max_value=50.0, value=2.5)
t3 = st.number_input("T3 (ng/mL)", min_value=0.0, max_value=5.0, value=1.4)
t4 = st.number_input("T4 (µg/dL)", min_value=0.0, max_value=15.0, value=8.0)

if st.button("Predict"):
    input_data = np.array([[tsh, t3, t4]])
    prediction = model.predict(input_data)[0]

    label_map = {0: "Hyperthyroidism", 1: "Hypothyroidism", 2: "Normal"}
    result = label_map.get(prediction, "Unknown")

    st.success(f"🧠 Prediction: {result}")

    if result == "Normal":
        st.info("Your thyroid levels appear normal. Keep monitoring regularly.")
    elif result == "Hypothyroidism":
        st.warning("Your TSH is high and T3/T4 are low. This may be hypothyroidism. Consult a doctor.")
    elif result == "Hyperthyroidism":
        st.warning("Your TSH is low and T3/T4 are high. This may be hyperthyroidism. Consult a doctor.")