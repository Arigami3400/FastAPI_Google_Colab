from fastapi import APIRouter
from colab_app.db.schema import AvocadoSchema
import joblib

model = joblib.load('colab_app/scaler_model/model_ava.pkl')
scaler = joblib.load('colab_app/scaler_model/scaler_ava.pkl')

avacado_router = APIRouter(prefix='/predict_avocado', tags=['/predict_avocado'])



@avacado_router.post('/')
async def predict(avocado: AvocadoSchema):
    avocado_dict = avocado.dict()

    new_color = avocado_dict.pop('color_category')
    color1_0 = [
        1 if new_color == 'green' else 0,
        1 if new_color == 'dark green' else 0,
        1 if new_color == 'purple' else 0,
    ]

    features = list(avocado_dict.values()) + color1_0
    scaled_data = scaler.transform([features])
    pred = model.predict(scaled_data)[0]
    if pred == 1:
        pred = 'Hard'
    elif pred == 2:
        pred = 'pre-conditioned'
    elif pred == 3:
        pred = 'breaking'
    elif pred == 4:
        pred = 'firm-ripe'
    else:
        pred = 'ripe'

    return {'predict': pred}



