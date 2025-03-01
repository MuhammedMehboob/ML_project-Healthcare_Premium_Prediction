import streamlit as st
from prediction_helper import predict


st.title("Insurance Prediction System")

# Creating Columns for Row Layout
col1, col2, col3 = st.columns(3)

# First Row
with col1:
    age = st.slider("Age", min_value=18, max_value=100, step=1, value=30)
with col2:
    number_of_dependants = st.slider("No. of Dependants", min_value=0, max_value=5, step=1, value=0)
with col3:
    income_lakhs = st.number_input("Income (in Lakhs)", min_value=0.0, max_value=100.0, step=0.1, value=5.0)

# Second Row
col4, col5, col6 = st.columns(3)
with col4:
    gender = st.selectbox("Gender", ["Male", "Female"])
with col5:
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])
with col6:
    marital_status = st.selectbox("Marital Status", ["Married", "Unmarried"])

# Third Row
col7, col8, col9 = st.columns(3)
with col7:
    bmi_category = st.selectbox("BMI Category", ["Normal", "Overweight", "Underweight", "Obesity"])
with col8:
    smoking_status = st.selectbox("Smoking Status", ["No Smoking", "Regular", "Occasional"])
with col9:
    employment_status = st.selectbox("Employment Status", ["Self-Employed", "Freelancer", "Salaried"])

# Fourth Row
col10, col11, col12 = st.columns(3)
with col10:
    medical_history = st.selectbox("Medical History", [
        "No Disease", "High blood pressure", "Diabetes",
        "Heart disease", "Thyroid", "Diabetes & High blood pressure",
        "Diabetes & Thyroid", "Diabetes & Heart disease", "High blood pressure & Heart disease"
    ])
with col11:
    insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
with col12:
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, step=1)

# Storing Inputs in a Dictionary
input_dict = {
    "age": age,
    "number_of_dependants": number_of_dependants,
    "income_lakhs": income_lakhs,
    "gender": gender,
    "region": region,
    "marital_status": marital_status,
    "bmi_category": bmi_category,
    "smoking_status": smoking_status,
    "employment_status": employment_status,
    "medical_history": medical_history,
    "insurance_plan": insurance_plan,
    "genetical_risk": genetical_risk
}

# Submit Button
st.markdown("---")
if st.button("Predict Insurance Amount"):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')
