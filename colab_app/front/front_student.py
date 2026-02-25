import streamlit as st
import requests

def check_student():
    st.title("Предсказание студента")
    api_url = "http://127.0.0.1:8000/predict_student"

    reading_score = st.number_input("Reading score", min_value=0, max_value=100)
    writing_score = st.number_input("Writing Score", 0, max_value=100)
    gender_male = st.selectbox("Пол", ["male", "female"])
    race_ethncity = st.selectbox("Группа", ["group A", "group B", "group C", "group D", "group E"])
    parental = st.selectbox("Образование родителей",
                            ["some high school", "high school", "associate", "bachelor", "master"])
    level = st.selectbox("Уровень", ["low", "medium", "high"])
    parental_level = st.selectbox("Поддержка", ["low", "medium", "high"])
    lunch = st.selectbox("Питание", ["standard", "free/reduced"])
    test = st.selectbox("Подготовка", ["none", "completed"])

    data = {
        "reading_score": reading_score,
        "writing_score": writing_score,
        "gender_male": gender_male,
        "race_ethncity": race_ethncity,
        "parental": parental,
        "parental_level": parental_level,
        "level": level,
        "lunch": lunch,
        "test": test
    }

    if st.button("Предсказать"):
        answer = requests.post(api_url, json=data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Результат: {result.get('predict')}')
        else:
            st.error(f'Ошибка: {answer.status_code}')
