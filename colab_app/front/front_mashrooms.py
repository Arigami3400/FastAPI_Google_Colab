import streamlit as st
import requests

def check_mashrooms():
    st.title("Предсказание гриба")

    api_url = "http://127.0.0.1:8000/predict_mashrooms"

    cap_shape = st.selectbox("Форма шляпки", ["b", "c", "x", "f", "k", "s"])
    cap_surface = st.selectbox("Поверхность шляпки", ["f", "g", "y", "s"])
    cap_color = st.selectbox("Цвет шляпки", ["n", "b", "c", "g", "r", "p", "u", "e", "w", "y"])
    bruises = st.selectbox("Синяки", ["t", "f"])
    odor = st.selectbox("Запах", ["a", "l", "c", "y", "f", "m", "n", "p", "s"])
    gill_attachment = st.selectbox("Крепление пластинок", ["a", "d", "f", "n"])
    gill_spacing = st.selectbox("Расстояние пластинок", ["c", "w", "d"])
    gill_size = st.selectbox("Размер пластинок", ["b", "n"])
    gill_color = st.selectbox("Цвет пластинок", ["k", "n", "b", "h", "g", "r", "o", "p", "u", "e", "w", "y"])
    stalk_shape = st.selectbox("Форма ножки", ["e", "t"])
    stalk_root = st.selectbox("Корень ножки", ["b", "c", "u", "e", "z", "r", "?"])
    stalk_surface_above_ring = st.selectbox("Поверхность ножки над кольцом", ["f", "y", "k", "s"])
    stalk_surface_below_ring = st.selectbox("Поверхность ножки под кольцом", ["f", "y", "k", "s"])
    stalk_color_above_ring = st.selectbox("Цвет ножки над кольцом", ["n", "b", "c", "g", "o", "p", "e", "w", "y"])
    stalk_color_below_ring = st.selectbox("Цвет ножки под кольцом", ["n", "b", "c", "g", "o", "p", "e", "w", "y"])
    veil_type = st.selectbox("Тип покрывала", ["p", "u"])
    veil_color = st.selectbox("Цвет покрывала", ["n", "o", "w", "y"])
    ring_number = st.selectbox("Количество колец", ["n", "o", "t"])
    ring_type = st.selectbox("Тип кольца", ["c", "e", "f", "l", "n", "p", "s", "z"])
    spore_print_color = st.selectbox("Цвет спор", ["k", "n", "b", "h", "r", "o", "u", "w", "y"])
    population = st.selectbox("Популяция", ["a", "c", "n", "s", "v", "y"])
    habitat = st.selectbox("Среда обитания", ["g", "l", "m", "p", "u", "w", "d"])

    data = {
        "cap_shape": cap_shape,
        "cap_surface": cap_surface,
        "cap_color": cap_color,
        "bruises": bruises,
        "odor": odor,
        "gill_attachment": gill_attachment,
        "gill_spacing": gill_spacing,
        "gill_size": gill_size,
        "gill_color": gill_color,
        "stalk_shape": stalk_shape,
        "stalk_root": stalk_root,
        "stalk_surface_above_ring": stalk_surface_above_ring,
        "stalk_surface_below_ring": stalk_surface_below_ring,
        "stalk_color_above_ring": stalk_color_above_ring,
        "stalk_color_below_ring": stalk_color_below_ring,
        "veil_type": veil_type,
        "veil_color": veil_color,
        "ring_number": ring_number,
        "ring_type": ring_type,
        "spore_print_color": spore_print_color,
        "population": population,
        "habitat": habitat
    }

    if st.button("Предсказать"):
        answer = requests.post(api_url, json=data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Результат: {result.get('predict')}')
        else:
            st.error(f'Ошибка: {answer.status_code}')



