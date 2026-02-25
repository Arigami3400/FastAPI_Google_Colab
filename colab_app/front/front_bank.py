
import streamlit as st
import requests

def check_bank():
    st.title('Bank Project')
    api_url = 'http://127.0.0.1:8000/predict_bank'

    person_age = st.number_input('Возраст', max_value=100.0, step=1.1)
    person_gender = st.selectbox('Пол', ['male', 'female'])
    person_education = st.selectbox('Образование', ['Bachelor', 'Doctorate', 'High_School', 'Master', 'Associate'])
    person_income = st.number_input('Дохот', step=500.0)
    person_emp_exp = st.number_input('Стаж', step=1)
    person_home_ownership = st.selectbox('Жилье', ['OTHER', 'OWN', 'RENT', 'MORTGAGE'])
    loan_amnt = st.number_input('Сумма кридита ', step=500.0)
    loan_intent = st.selectbox('Цель Кридита',
                               ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE', 'DEBTCONSOLIDATION',
                                'EDUCA'])
    loan_int_rate = st.number_input('Процентная ставка', )
    loan_percent_income = st.number_input('Доход и кредит', max_value=1.0)
    cb_person_cred_hist_length = st.number_input('Длина кредитной истории', min_value=1, step=1)
    credit_score = st.number_input('Кредитный бал', min_value=1, step=10)
    previous_loan_defaults_on_file = st.selectbox('Дефолт', ['Yes', 'NO'])

    bank_data = {
        "person_age": person_age,
        "person_gender": person_gender,
        "person_education": person_education,
        "person_income": person_income,
        "person_emp_exp": person_emp_exp,
        "person_home_ownership": person_home_ownership,
        "loan_amnt": loan_amnt,
        "loan_intent": loan_intent,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": cb_person_cred_hist_length,
        "credit_score": credit_score,
        "previous_loan_defaults_on_file": previous_loan_defaults_on_file
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=bank_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f'Результат: {result.get("predict")}')
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подкючиться к API')
