import streamlit as st
import requests

def check_avocado():
    st.title("Определение спелости авокадо")

    api_url = "http://127.0.0.1:8000/predict_avocado"

    firmness = st.number_input("Твёрдость", 0.0)
    hue = st.number_input("тон цвета", 0)
    saturation = st.number_input('насыщенность', 0)
    brightness = st.number_input('яркость', 0)
    color_category = st.selectbox("Категория цвета", ["green", "dark green", "purple"])
    sound_db = st.number_input("Звук при постукивании ", 0)
    weight_g = st.number_input("Вес: граммы", 0)
    size_cm3 = st.number_input("Объем ", 0)

    data = {
        "firmness": firmness,
        "hue": hue,
        "saturation": saturation,
        "brightness": brightness,
        "color_category": color_category,
        "sound_db": sound_db,
        "weight_g": weight_g,
        "size_cm3": size_cm3
    }

    if st.button("Предсказать"):
        answer = requests.post(api_url, json=data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Результат: {result.get('predict')}')
        else:
            st.error(f'Ошибка: {answer.status_code}')
