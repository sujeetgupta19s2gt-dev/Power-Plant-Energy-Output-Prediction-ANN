import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# --- Step 1: Load the trained model and scaler ---
model = load_model('ann_model.h5')
scaler = joblib.load('scaler.pkl')

# --- Step 2: Page Title & Description ---
st.title("⚡ Power Plant Energy Predictor")
st.write("Welcome! This simple web app predicts the Net Hourly Electrical Energy Output (**PE**) of a Combined Cycle Power Plant based on ambient environmental conditions.")

st.markdown("---")

# --- Step 3: Input Controls (Beginner Friendly Form) ---
st.header("1. Enter Plant Conditions")

col1, col2 = st.columns(2)

with col1:
    at = st.number_input("Ambient Temperature (AT) in °C", min_value=0.0, max_value=50.0, value=15.0)
    v = st.number_input("Exhaust Vacuum (V) in cm Hg", min_value=20.0, max_value=100.0, value=40.0)

with col2:
    ap = st.number_input("Ambient Pressure (AP) in millibar", min_value=900.0, max_value=1100.0, value=1010.0)
    rh = st.number_input("Relative Humidity (RH) in %", min_value=0.0, max_value=100.0, value=75.0)

# Average PE benchmark from the dataset (~454 MW)
AVERAGE_PE = 454.36 

st.markdown("---")

# --- Step 4: Prediction & Output Graph ---
st.header("2. Prediction & Analysis")

if st.button("Predict Energy Output"):
    # Preprocess inputs
    features = np.array([[at, v, ap, rh]])
    scaled_features = scaler.transform(features)
    
    # Model prediction
    prediction = model.predict(scaled_features)
    predicted_pe = float(prediction[0][0])
    
    # Display Result
    st.success(f"**Predicted Energy Output (PE):** {predicted_pe:.2f} MW")
    
    # Simple Visualisation Graph comparing prediction to benchmark average
    st.subheader("Comparison with Average Power Plant Output")
    
    chart_data = pd.DataFrame({
        "Output Type": ["Average Output", "Your Prediction"],
        "Energy Output (MW)": [AVERAGE_PE, predicted_pe]
    })
    
    st.bar_chart(chart_data.set_index("Output Type"))
    
    # Quick human-like commentary
    if predicted_pe > AVERAGE_PE:
        st.info("💡 Note: Your predicted output is **above** average due to cooler ambient temperature or lower exhaust vacuum.")
    else:
        st.info("💡 Note: Your predicted output is **below** average, likely due to high ambient temperature.")