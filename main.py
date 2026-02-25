
from colab_app.api import avocado, bank,diabet , house , mashrooms, student, titanic, telecom
from fastapi import FastAPI
import uvicorn

colab_app = FastAPI()
colab_app.include_router(avocado.avacado_router)
colab_app.include_router(bank.bank_router)
colab_app.include_router(diabet.diabet_router)
colab_app.include_router(house.house_router)
colab_app.include_router(mashrooms.mashrooms_router)
colab_app.include_router(student.student_router)
colab_app.include_router(titanic.titanic_router)
colab_app.include_router(telecom.telecom_router)


if __name__ == '__main__':
    uvicorn.run(colab_app, host='127.0.0.1', port=8000)


