from fastapi import APIRouter
import joblib
from colab_app.db.schema import DiabetSchema

diabet_router = APIRouter(prefix='/predict_diabet', tags=['/predict_diabet'])

model = joblib.load('colab_app/scaler_model/model_dia.pkl')
scaler = joblib.load('colab_app/scaler_model/scaler_dia.pkl')



@diabet_router.post('/')
async def predict(diabet: DiabetSchema):
    diabet_dict = diabet.dict()

    features = list(diabet_dict.values())
    scaled_data = scaler.transform([features])
    print(model.predict(scaled_data))
    pred = model.predict(scaled_data)[0]
    if pred == 1:
        pred = 'Диабет'
    else:
        pred = 'Нет Диабета'
    return {'Predict': pred}


