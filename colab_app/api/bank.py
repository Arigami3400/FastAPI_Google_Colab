from fastapi import APIRouter
from colab_app.db.schema import BankPredict1Schema
import joblib

scaler = joblib.load('colab_app/scaler_model/scaler_bank.pkl')
model = joblib.load('colab_app/scaler_model/model_bank.pkl')

bank_router = APIRouter(prefix='/predict_bank', tags=['predict_bank'])





@bank_router.post('/')
async def predict1(bank: BankPredict1Schema):
    bank_dict = bank.dict()
    keys = [
        'person_gender',
        'person_education',
        'loan_intent',
        'previous_loan_defaults_on_file',
        'person_home_ownership'
    ]

    new_bank = {}
    for k in keys:
        new_bank[k] = bank_dict.pop(k)


    person_gender1_0 = [
        1 if new_bank == 'male' else 0,
    ]

    person_education1_0 = [
        1 if new_bank == 'Bachelor' else 0,
        1 if new_bank == 'Doctorate' else 0,
        1 if new_bank == 'High_School' else 0,
        1 if new_bank == 'Master' else 0,
    ]

    person_home1_0 = [
        1 if new_bank == 'OTHER' else 0,
        1 if new_bank == 'OWN' else 0,
        1 if new_bank == 'RENT' else 0,
    ]

    loan_intent1_0 = [
        1 if new_bank == 'HOMEIMPROVEMENT' else 0,
        1 if new_bank == 'MEDICAL' else 0,
        1 if new_bank == 'PERSONAL' else 0,
        1 if new_bank == 'VENTURE' else 0,
        1 if new_bank == 'EDUCATION' else 0,
    ]

    previous_loan_defaults_on_file1_0 = [
        1 if new_bank == 'Yes' else 0,
    ]


    features = list(bank_dict.values()) +person_gender1_0 + person_education1_0 + person_home1_0 + loan_intent1_0 + previous_loan_defaults_on_file1_0
    scaled_data = scaler.transform([features])
    pred = model.predict(scaled_data)[0]
    if pred == 1:
        pred = 'Разрешено'
    else:
        pred = 'Запрешено'

    return {"predict": pred}
