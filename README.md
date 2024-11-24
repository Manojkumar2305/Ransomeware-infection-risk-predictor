Ransomware Infection Risk Predictor :

This web application helps users predict the likelihood of a ransomware infection based on their behavior. It uses a Multiple Linear Regression model to estimate the infection risk based on factors like phishing email clicks, software updates, antivirus usage, and USB device usage.

Project Overview
The goal of this project is to:
Educate users on how their online behavior can affect their risk of ransomware infection.
Provide a predictive model to estimate the risk of infection based on user-provided data.
Share educational tips on improving user behavior to lower the risk of infection.
Features

User Input: The application takes the following user input through a sidebar:

->Number of phishing emails clicked
->Frequency of software updates
->Whether the user is using antivirus software
->Number of external USB devices used
->Prediction: The model predicts the infection risk, with a score between 0 and 1:

0 means low risk, and 1 means high risk.

Educational Tips: Based on the predicted risk, the app provides advice to help users reduce the risk of infection:

High Risk: Warning messages about avoiding suspicious links and ensuring software is regularly updated.
Moderate Risk: Informative tips on improving user behavior.
Low Risk: Encouragement to continue practicing good cybersecurity habits.
