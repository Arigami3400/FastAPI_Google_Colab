from fastapi import APIRouter
import joblib
from colab_app.db.schema import TitanicSchema
from pydantic import BaseModel
titanic_router = APIRouter(prefix='/predict_titanic', tags=['/predict_titanic'])

model = joblib.load('model_tita.pkl')
scaler = joblib.load('scaler_tita.pkl')



@titanic_router.post('/predict')
async def predict(titanic: TitanicSchema):
    titanic_dict = titanic.dict()

    new_embarked = titanic_dict.pop('Embarked')
    embarked1_0 = [
        1 if new_embarked == 'S' else 0,
        1 if new_embarked == 'Q' else 0,
    ]

    new_sex = titanic_dict.pop('Sex')
    sex1_0 = [
        1 if new_sex == 'male' else 0,

    ]

    features = list(titanic_dict.values()) + embarked1_0 + sex1_0
    scaled_data = scaler.transform([features])
    print(model.predict(scaled_data))
    pred = model.predict(scaled_data)[0]
    if pred == 0:
        pred = "Не Выжил"
    else:
        pred = "Выжил"
    return {'predict': pred}



