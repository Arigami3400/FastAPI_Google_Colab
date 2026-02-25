import streamlit as st
import requests

def check_titanic():
    st.title("Предсказание выживания (Titanic)")
    api_url = "http://127.0.0.1:8000/predict_titanic"

    Embarked = st.selectbox("Порт посадки", ["C", "Q", "S"])
    Fare = st.number_input("Стоимость билета", 0.0)
    Parch = st.number_input("Родители/дети на борту", 0)
    SibSp = st.number_input("Братья/сестры или супруги", 0)
    Age = st.number_input("Возраст", 0.0)
    Sex = st.selectbox("Пол", ["male", "female"])
    Pclass = st.selectbox("Класс билета", [1, 2, 3])

    data = {
        "Embarked": Embarked,
        "Fare": Fare,
        "Parch": Parch,
        "SibSp": SibSp,
        "Age": Age,
        "Sex": Sex,
        "Pclass": Pclass
    }

    if st.button("Предсказать"):
        answer = requests.post(api_url, json=data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Результат: {result.get('predict')}')
        else:
            st.error(f'Ошибка: {answer.status_code}')
