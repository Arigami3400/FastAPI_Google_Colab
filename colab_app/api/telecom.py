from fastapi import APIRouter
from colab_app.db.schema import TelecomSchema
from pydantic import BaseModel
import joblib

telecom_router = APIRouter(prefix='/predict_telecom', tags=['/predict_telecom'])

scaler = joblib.load('scaler_tele.pkl')
model = joblib.load('model_tele.pkl')


Paymentmethod_list = ['Credit_card_automatic', 'Electronic_check', 'Mailed_check']
Contract_list = ['One_year', 'Two_year']
InternetService_list = ['Fiber_optic', 'No']
MultipleLines_list = ['No_phone_service', 'Yes']

@telecom_router.post('/predict')
async def predict(telecom: TelecomSchema):
    tel_dict = telecom.dict()
    new_pay = tel_dict.pop('PaymentMethod')
    new_contract = tel_dict.pop('Contract')
    new_inte= tel_dict.pop('InternetService')
    new_multi= tel_dict.pop('MultipleLines')
    new_gender = tel_dict.pop('gender')
    new_part = tel_dict.pop('Partner')
    new_depend = tel_dict.pop('Dependents')
    new_pservice = tel_dict.pop('PhoneService')
    new_paper = tel_dict.pop('PaperlessBilling')
    new_onlsecurity = tel_dict.pop('OnlineSecurity')
    new_onlbackup = tel_dict.pop('OnlineBackup')
    new_device = tel_dict.pop('DeviceProtection')
    new_tesh = tel_dict.pop('TechSupport')
    new_streamtv = tel_dict.pop('StreamingTV')
    new_streamm = tel_dict.pop('StreamingMovies')

    pay1_0 = [1 if new_pay == i else 0 for i in Paymentmethod_list]
    cont1_0 = [1 if new_contract == i else 0 for i in Contract_list]
    inter1_0 = [1 if new_inte == i else 0 for i in InternetService_list]
    multi1_0 = [1 if new_multi == i else 0 for i in MultipleLines_list]

    gender1_0 = [1 if new_gender == 'Female' else 0]
    new_part = [1 if new_part == 'Yes' else 0]
    new_depend = [1 if new_depend == 'Yes' else 0]
    new_pservice1_0 = [1 if new_pservice == 'Yes' else 0]
    new_paper1_0 = [1 if new_paper == 'Yes' else 0]
    new_onlsecurity1_0 = [1 if new_onlsecurity == 'Yes' else 0]
    new_onlbackup1_0 = [1 if new_onlbackup == 'Yes' else 0]
    new_device1_0 = [1 if new_device == 'Yes' else 0]
    new_tesh1_0 = [1 if new_tesh == 'Yes' else 0]
    new_streamtv1_0 = [1 if new_streamtv == 'Yes' else 0]
    new_streamm1_0 = [1 if new_streamm == 'Yes' else 0]


    features = [list(tel_dict.values())  +gender1_0 +new_part +new_depend
                +new_pservice1_0 +new_paper1_0 +new_onlsecurity1_0
                +new_onlbackup1_0 +new_device1_0 +new_tesh1_0 +new_streamtv1_0
                +new_streamm1_0 + pay1_0 + cont1_0 + inter1_0  + multi1_0]
    scaled_data = scaler.transform(features)
    pred = model.predict(scaled_data)[0]
    if pred == 1:
        pred = 'Останется'
    else:
        pred = 'Уйдет'
    return {"predict": pred}













