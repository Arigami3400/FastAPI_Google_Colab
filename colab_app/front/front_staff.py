import streamlit as st
import requests

def check_staff():
    st.title('Предсказание работников')
    api_url = "http://127.0.0.1:8000/predict_staff/"

    age_front = st.slider('Возраст', min_value=18, max_value=70)
    business_travel_front = st.selectbox('Командировка', ['Travel_Rarely', 'Travel_Frequently'])
    daily_rate_front = st.number_input('Дневная ставка оплаты', min_value=100, max_value=10000, step=100)
    Departament_front = st.selectbox("Отдел", ['Research & Development', 'Sales'])
    distance_home_front = st.number_input('Дистанция до Дома', step=5)
    Education_front = st.number_input('Уровень образования', min_value=1, max_value=10)
    Education_Field_front = st.selectbox('Область Образования',['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree'])
    environment_satisfaction_front = st.number_input('Удовлетворённость рабочей средой', min_value=1, max_value=5)
    gender_front = st.selectbox('Пол', ['Female', 'Male'])
    hourly_rate_front = st.number_input('Почасовая ставка', min_value=1, max_value=100)
    job_involvement_front = st.number_input('Вовлечённость в работу', min_value=1, max_value=100)
    job_level_front = st.number_input('Уровень работы', min_value=1, max_value=10)
    Job_role_front = st.selectbox('Роль на Работе',['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director','Research Director', 'Research Scientist', 'Sales Executive','Sales Representative'])
    job_satisfaction_front = st.number_input('Удовлетворённость работой', min_value=1, step=1)
    marital_status_front = st.selectbox('Семейное положение', ['Married', 'Single'])
    monthly_income_front = st.number_input('Месячный доход', min_value=1, max_value=10000)
    monthly_rate_front = st.number_input('Месячная ставка оплаты', min_value=1, max_value=10000)
    num_companies_worked_front = st.number_input('Количество компаний, где работал', min_value=1, max_value=20)
    over_time_front = st.selectbox('Сверхурочная работа', ['Yes', 'No'])
    percent_salary_hike_front = st.number_input('Процент повышения зарплаты')
    performance_rating_front = st.number_input('Оценка производительности')
    relationship_satisfaction_front = st.number_input('Удовлетворённость отношениями в коллективе')
    stockoption_level_front = st.number_input('Уровень опционов на акции')
    total_working_years_front = st.number_input('Общий стаж работы')
    training_times_last_year_front = st.number_input('Количество обучений за прошлый год')
    work_life_balance_front = st.number_input('Баланс работа-жизнь')
    years_atcompany_front = st.number_input('Лет в текущей компании')
    years_incurrent_role_front = st.number_input('Лет в текущей должности')
    years_since_last_promotion_front = st.number_input('Лет с последнего повышения')
    years_with_curr_manager_front = st.number_input('Лет с текущим менеджером')

    data = {
        "age": age_front,
        "business_travel": business_travel_front,
        "daily_rate": daily_rate_front,
        "department": Departament_front,
        "distance_from_home": distance_home_front,
        "education": Education_front,
        "education_field": Education_Field_front,
        "environment_satisfaction": environment_satisfaction_front,
        "gender": gender_front,
        "hourly_rate": hourly_rate_front,
        "job_involvement": job_involvement_front,
        "job_level": job_level_front,
        "job_role": Job_role_front,
        "job_satisfaction": job_satisfaction_front,
        "marital_status": marital_status_front,
        "monthly_income": monthly_income_front,
        "monthly_rate": monthly_rate_front,
        "num_companies_worked": num_companies_worked_front,
        "over_time": over_time_front,
        "percent_salary_hike": percent_salary_hike_front,
        "performance_rating": performance_rating_front,
        "relationship_satisfaction": relationship_satisfaction_front,
        "stockoption_level": stockoption_level_front,
        "total_working_years": total_working_years_front,
        "training_times_lastyear": training_times_last_year_front,
        "work_life_balance": work_life_balance_front,
        "years_atcompany": years_atcompany_front,
        "years_incurrent_role": years_incurrent_role_front,
        "years_since_lastpromotion": years_since_last_promotion_front,
        "years_with_currmanager": years_with_curr_manager_front

    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f'Результат: {result.get("predict")}')
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подкючиться к API')


