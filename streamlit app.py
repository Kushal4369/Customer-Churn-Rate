import streamlit as st
import pandas as pd
import joblib

model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("📉 Customer Churn Prediction App")

st.write("Enter customer details:")

tenure = st.number_input("Tenure (months)", 0, 100)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

# Encode contract manually (same as LabelEncoder order)
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
contract_encoded = contract_map[contract]

input_data = pd.DataFrame([[tenure, monthly_charges, total_charges, contract_encoded]],
                          columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract'])

# input_scaled = scaler.transform(input_data)

# if st.button("Predict"):
#     pred = model.predict(input_scaled)[0]
#     st.success("✅ Customer will stay" if pred == 0 else "⚠️ Customer likely to churn")
