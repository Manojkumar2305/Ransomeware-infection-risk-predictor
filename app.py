import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Title
st.title("Ransomware Infection Risk Predictor")

# Sidebar for user input
st.sidebar.header("Input User Behavior Data")
phishing_clicks = st.sidebar.slider("Phishing Emails Clicked", 0, 50, 5)
software_updates = st.sidebar.slider("Frequency of Software Updates (per month)", 0, 10, 2)
antivirus_use = st.sidebar.selectbox("Using Antivirus?", ["Yes", "No"])
usb_devices = st.sidebar.slider("Number of External USB Devices Used", 0, 10, 1)

# Encode antivirus_use
antivirus_flag = 1 if antivirus_use == "Yes" else 0

# Prepare data for prediction
data = np.array([[phishing_clicks, software_updates, antivirus_flag, usb_devices]])

# Dummy data for training the model (replace with actual data)
X_dummy = np.array([[5, 2, 1, 1], [10, 1, 0, 3], [2, 5, 1, 0], [15, 0, 0, 5]])
y_dummy = np.array([0.2, 0.8, 0.1, 0.9])  # Example target values (risk levels)

# Train a simple Linear Regression model
model = LinearRegression()
model.fit(X_dummy, y_dummy)

# Prediction
risk = model.predict(data)[0]
st.subheader(f"Predicted Infection Risk: {risk:.2f}")

# Educational tips based on the risk level
if risk > 0.7:
    st.warning("High risk! Avoid clicking unknown links and update your software regularly.")
elif risk > 0.4:
    st.info("Moderate risk. Improve your behavior to reduce risk.")
else:
    st.success("Low risk! Keep following good practices.")

