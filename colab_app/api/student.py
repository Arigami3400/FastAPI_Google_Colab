from fastapi import APIRouter
from colab_app.db.schema import *
import joblib

model = joblib.load('colab_app/scaler_model/model_stu.pkl')
scaler = joblib.load('colab_app/scaler_model/scaler_stu.pkl')


student_router = APIRouter(prefix='/predict_student', tags=['/predict_student'])



@student_router.post('/')
async def predict(student: StudentSchema):
    student_dict = student.dict()

    new_gender = student_dict.pop('gender_male')
    new_race = student_dict.pop('race_ethncity')
    new_parental = student_dict.pop('parental')
    new_level = student_dict.pop('level')
    new_parental_level = student_dict.pop('parental_level')
    new_lunch = student_dict.pop('lunch')
    new_test = student_dict.pop('test')

    gender1_0 = [
        1 if new_gender == 'male' else 0,
    ]

    race1_0 = [
        1 if new_race == 'B' else 0,
        1 if new_race == 'C' else 0,
        1 if new_race == 'D' else 0,
        1 if new_race == 'E' else 0,
    ]

    parental1_0 = [
        1 if new_parental == "bachelor's degree" else 0,
        1 if new_parental == "high school" else 0,
        1 if new_parental == "master's degree" else 0,
    ]

    level1_0 = [
        1 if new_level == "college" else 0,
    ]

    parental_level1_0 = [
        1 if new_parental_level == "high school" else 0,
    ]

    lunch1_0 = [
        1 if new_lunch == 'standard' else 0,
    ]
    test1_0 = [
        1 if new_test == 'none' else 0,
    ]

    features = list(student_dict.values()) + gender1_0 + race1_0 +parental1_0 + level1_0 + parental_level1_0 + lunch1_0 + test1_0
    scaled_data = scaler.transform([features])
    pred = model.predict(scaled_data)[0]
    return {'predict': round(pred, 2)}