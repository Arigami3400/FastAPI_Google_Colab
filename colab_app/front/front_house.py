import streamlit as st
import requests

def check_house():
    st.title("Предсказание цены дома")
    api_url = "http://127.0.0.1:8000/predict_house"

    GrLivArea = st.number_input("Жилая площадь", min_value=0, value=1, step=2)
    YearBuilt = st.number_input("Год постройки", min_value=1900, max_value=2026, step=1)
    GarageCars = st.number_input("Машин в гараже", min_value=0, step=1)
    TotalBsmtSF = st.number_input("Площадь подвала", min_value=0, max_value=1000, step=1)
    FullBat = st.number_input("Количество ванных", min_value=0, max_value=10, step=1)
    OverallQual = st.slider("Качество", min_value=1, max_value=10)
    Neighborhood = st.text_input("Район")

    house_data = {
        "GrLivArea": GrLivArea,
        "YearBuilt": YearBuilt,
        "GarageCars": GarageCars,
        "TotalBsmtSF": TotalBsmtSF,
        "FullBat": FullBat,
        "OverallQual": OverallQual,
        "Neighborhood": Neighborhood,
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=house_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f'Результат: {result.get("Price")}')
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подкючиться к API')

