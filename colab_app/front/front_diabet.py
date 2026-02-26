import streamlit as st
import requests

def check_diabet():
    st.title('Определение Диабета')

    api_ulr = 'http://127.0.0.1:8000/predict_diabet'

    pregnancies = st.number_input("Беременности", min_value=0, step=1)
    glucose = st.number_input("Глюкоза", min_value=0, step=1)
    blood_pressure = st.number_input("Артериальное давление", min_value=0, step=1)
    skin_thickness = st.number_input("Толщина кожи", min_value=0, step=1)
    insulin = st.number_input("Инсулин", min_value=0, step=1)
    bmi = st.number_input("Индекс массы тела (BMI)", min_value=0.0)
    dpf = st.number_input("Функция наследственной предрасположенности к диабету", min_value=0.0)
    age = st.number_input("Возраст", min_value=0, max_value=70, step=1)

    diabet_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_ulr, json=diabet_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f'Результат: {result.get("Predict")}')
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подкючиться к API')
