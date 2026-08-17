import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="Loan Status Predictor",
    page_icon="🏦",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("./models/model.pkl", 'rb') as file:
        return pickle.load(file)

model= load_model()

st.title("🏦 Loan Status Predictor")

st.write(
    "Enter the applicant's information below to estimate "
    "the probability of loan approval."
)

with st.form("loan_form"):
    st.subheader("Applicant Information")
    col1, col2 = st.columns(2)
    with col1:
        gndr = st.selectbox(label="Gender", options=["Male", "Female"])
        mar = st.selectbox(label="Marital Status", options=["Married", "Unmarried"])
        dep = st.selectbox(label="Number of Dependants", options=["0", "1", "2", "3+"])
        se = st.selectbox("Employment", options=["Employed", "Self Employed"])
        ed = st.selectbox("Education", options=["Not Graduate", "Graduate"])
        pa = st.selectbox("Property Area", options=["Urban", "Rural", "Semi-Urban"])

    with col2:
        applicant_income = st.number_input("Applicant Income", min_value=0, max_value=100000, step=1000, value=5000)
        coapplicant_income = st.number_input("Co-Applicant Income", min_value=0, max_value=100000, step=1000, value=5000)
        loan_amount = st.number_input("Loan Amount", min_value=0, max_value=1000, step=100, value= 400)
        loan_amount_term = st.select_slider("Loan Amount Term", options=[12, 36, 60, 84, 120, 180, 240, 300, 360, 480], value=360)
        ch = st.selectbox("Credit History", options=["No Credit History", "Credit History Exists"])
        submit = st.form_submit_button("Predict Loan Status")

if submit:
    gender = 0 if gndr == "Female" else 1
    married = 0 if mar=="Unmarried" else 1
    self_employed = 0 if se=="Employed" else 1
    education = 0 if ed == "Not Graduate" else 1
    urban = 1 if pa=="Urban" else 0
    semi_urban = 1 if pa=="Semi-Urban" else 0
    credit_history = 0 if ch == "No Credit History" else 1
    dependents_map = {"0": 0, "1": 1, "2": 2, "3+": 3}
    dependents = dependents_map[dep]


    input_data = pd.DataFrame([{
        'Married': married, 
        'Dependents': dependents, 
        'ApplicantIncome': applicant_income, 
        'CoapplicantIncome': coapplicant_income, 
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term, 
        'Credit_History': credit_history, 
        'Semiurban': semi_urban, 
        'Urban': urban
    }])
    
    proba = model.predict_proba(input_data)[0,1]
    st.divider()
    st.subheader("Prediction Result")
    st.metric("Loan Approval Probability", f"{proba:.1%}")
    st.progress(float(proba))

    if proba <0.7:
        st.error("Loan is likely to be denied.")
    else:
        st.success("Loan is likely to be sanctioned.")