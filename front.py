import streamlit as st
import requests

api_url = 'http://127.0.0.1:8008/predict'

st.title('Diabet Test')

Pregnancies = st.number_input('Pregnancies', min_value=0.0, step=0.1)
Glucose = st.number_input('Glucose', min_value=0.0, step=0.1)
BloodPressure = st.number_input('BloodPressure', min_value=0.0, step=0.1)
SkinThickness = st.number_input('SkinThickness', min_value=0.0, step=0.1)
Insulin = st.number_input('Insulin', min_value=0.0, step=0.1)
BMI = st.number_input('BMI', min_value=0.0, step=0.1)
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, step=0.1)
Age = st.number_input('Age', min_value=0.0, step=0.1)

diabet_data = {
    'Pregnancies': Pregnancies,
    'Glucose': Glucose,
    'BloodPressure': BloodPressure,
    'SkinThickness': SkinThickness,
    'Insulin': Insulin,
    'BMI': BMI,
    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
    'Age': Age,
}



if st.button('Predict'):
    try:
        answer = requests.post(api_url, json=diabet_data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f"Predict: {result.get('Predict')}")
        else:
            st.error(f"Ошибка: {answer.status_code}")
    except requests.exceptions.RequestException:
        st.error("Ошибка подключения к API")