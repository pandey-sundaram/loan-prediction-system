import streamlit as st
import pandas as pd
import joblib

# 1. Load the simplified model
model = joblib.load('web_model.pkl')

# 2. Build the UI
st.title("🏦 Loan Default Prediction App")
st.write("Enter the applicant's details below to check their loan risk.")

# 3. Create input fields for the user
col1, col2 = st.columns(2)

with col1:
    annual_income = st.number_input("Annual Income ($)", min_value=0, value=50000)
    loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=10000)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=40.0, value=10.5)

with col2:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=700)
    dti = st.number_input("Debt-to-Income Ratio (e.g., 0.20)", min_value=0.0, max_value=1.0, value=0.20)

# 4. Create a button to make predictions
if st.button("Predict Loan Status"):
    
    # Put the inputs into a dictionary (must match the exact order of web_features)
    user_data = {
        'annual_income': [annual_income],
        'credit_score': [credit_score],
        'loan_amount': [loan_amount],
        'debt_to_income_ratio': [dti],
        'interest_rate': [interest_rate]
    }
    
    # Convert to a DataFrame
    user_df = pd.DataFrame(user_data)
    
    # Make prediction
    prediction = model.predict(user_df)
    
    # Show the result!
    st.markdown("---")
    if prediction[0] == 1:
        st.success("✅ **APPROVED:** This applicant is low risk and likely to pay back the loan.")
    else:
        st.error("⚠️ **HIGH RISK:** This applicant is likely to default. Rejection recommended.")