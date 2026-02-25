import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from colab_app.front.front_house import check_house
from colab_app.front.front_student import check_student
from colab_app.front.front_titanic import check_titanic
from colab_app.front.front_bank import check_bank
from colab_app.front.front_mashrooms import check_mashrooms
from colab_app.front.front_diabet import check_diabet
from colab_app.front.front_avocado import check_avocado
from colab_app.front.front_telecom import check_telecom

with st.sidebar:
    name = st.radio('ML models:', ['Info', 'House', 'Student', 'Titanic', 'Bank',
                                   'Mashrooms', 'Diabet', 'Avocado', 'Telecom'])

if name =='Info':
    st.title('Welcome')
    st.text('Student — предсказание успеваемости студентов')
    st.text('Titanic — предсказание выживаемости на борту корабля')
    st.text('House — предсказание стоимости недвижимости')
    st.text('Bank — банковская аналитика')
    st.text('Diabet — диагностика диабета')
    st.text('Avocado — предсказание зрелости авокадо')
    st.text('Mushroom — классификация грибов')
    st.text('Telecom — отток клиентов телеком')


elif name == 'House':
    check_house()

elif name == 'Student':
    check_student()

elif name == 'Titanic':
    check_titanic()

elif name == 'Bank':
    check_bank()

elif name == 'Mashrooms':
    check_mashrooms()

elif name == 'Diabet':
    check_diabet()

elif name == 'Avocado':
    check_avocado()

elif name == 'Telecom':
    check_telecom()


