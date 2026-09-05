# ⚡ Power Plant Electrical Energy Output Prediction (ANN Regression)

An end-to-end deep learning regression pipeline built with **Keras / TensorFlow** and deployed as an interactive web application with **Streamlit** to estimate the net hourly electrical power output ($PE$) of a combined-cycle power plant based on ambient environmental conditions.

---

## 🌐 Live Web Application

Try the interactive predictor online:  
👉 **[Power Plant Energy Predictor Web App](https://power-plant-energy-output-prediction-ann-d7tsamewka5g2stg3suqb.streamlit.app/)**

---

## 📌 Project Overview

Operating a combined-cycle power plant efficiently relies heavily on understanding how environmental factors impact total power generation. This project uses real-world sensor data (`powerplant_data.csv`) to train a multi-layer Artificial Neural Network (ANN) that captures non-linear interactions between weather variables and energy output.

The trained pipeline is deployed using Streamlit to provide real-time power predictions alongside benchmark visualization against dataset averages.

---

## 📊 Dataset & Features

The model uses 9,568 hourly observations collected from a Combined Cycle Power Plant over six years.

### Target Variable:
* **PE** — Net hourly electrical energy output (**Megawatts, MW**)

### Input Features:
* **AT** — Ambient Temperature (°C)
* **V** — Exhaust Vacuum (cm Hg)
* **AP** — Ambient Pressure (millibar)
* **RH** — Relative Humidity (%)

---

## 🏗️ Model Architecture & Tech Stack

* **Machine Learning Framework:** Keras / TensorFlow (`ann_model.h5`)
* **Preprocessing:** `scikit-learn` `StandardScaler` (`scaler.pkl`) fitted on training data to prevent data leakage
* **Web Interface:** Streamlit (`app.py`)
* **Deployment Platform:** Streamlit Community Cloud (Python 3.11 runtime)

---

## 🚀 Live App Features

* **Interactive Form Controls:** Enter environmental parameters ($AT$, $V$, $AP$, $RH$) directly into the dashboard.
* **Real-time Prediction:** Generates $PE$ predictions instantly using the saved neural network model and feature scaler.
* **Visual Comparison Graph:** Displays a dynamic bar chart comparing the predicted output against the historical power plant benchmark average (~454.36 MW).
* **Automated Insights:** Displays quick context feedback explaining whether conditions favor above-average or below-average power generation.

---

## 🛠️ Getting Started (Local Setup)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sujeetgupta19s2gt-dev/Power-Plant-Energy-Output-Prediction-ANN.git](https://github.com/sujeetgupta19s2gt-dev/Power-Plant-Energy-Output-Prediction-ANN.git)
   cd Power-Plant-Energy-Output-Prediction-ANN
