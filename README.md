# ⚡ Power Plant Electrical Energy Output Prediction (ANN Regression)

An end-to-end deep learning regression pipeline built with **PyTorch** to estimate the net hourly electrical power output ($PE$) of a combined-cycle power plant based on ambient environmental conditions.

---

## 📌 Project Overview

Operating a combined-cycle power plant efficiently relies heavily on understanding how environmental factors impact total power generation. This project uses real-world sensor data (`powerplant_data.csv`) to train a multi-layer Artificial Neural Network (ANN) that captures non-linear interactions between weather variables and energy output.

---

## 📊 Dataset & Features

The model uses **9,568 hourly observations** collected from a Combined Cycle Power Plant over six years.

* **Target Variable:**
  * `PE` — Net hourly electrical energy output (**Megawatts, MW**)

* **Input Features:**
  * `AT` — Ambient Temperature (°C)
  * `V` — Exhaust Vacuum (cm Hg)
  * `AP` — Ambient Pressure (millibar)
  * `RH` — Relative Humidity (%)

---

## 🏗️ Model Architecture & Training Setup

* **Framework:** PyTorch (`torch.nn`)
* **Architecture:** Multi-Layer Perceptron (MLP) tuned for continuous tabular regression
* **Data Preprocessing:** Standardized continuous features using `StandardScaler` fitted on training data to prevent data leakage
* **Activation:** Rectified Linear Unit (**ReLU**) across hidden layers for learning non-linear patterns
* **Optimization:** **Adam** optimizer paired with **Mean Squared Error (MSE)** loss

---

## 📈 Results & Evaluation

Evaluated on an **80/20 train-test split** (1,914 holdout evaluation samples):

| Metric | Result |
| :--- | :--- |
| **$R^2$ Score** | **0.9343 (93.43% variance explained)** |
| **Test Set Size** | 1,914 samples |

### Sample Predictions vs. Actual Output

| Sample | Predicted ($PE$) | Actual ($PE$) | Delta ($\Delta$) |
| :---: | :---: | :---: | :---: |
| **1** | 435.19 MW | 433.27 MW | +1.92 MW |
| **2** | 436.82 MW | 438.16 MW | -1.34 MW |
| **3** | 461.23 MW | 458.42 MW | +2.81 MW |
| **4** | 476.37 MW | 480.82 MW | -4.45 MW |

---

## 🛠️ Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Power-Plant-Energy-Output-Prediction-ANN.git](https://github.com/YOUR_USERNAME/Power-Plant-Energy-Output-Prediction-ANN.git)
   cd Power-Plant-Energy-Output-Prediction-ANN
