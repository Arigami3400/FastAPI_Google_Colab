from fastapi import APIRouter
import joblib

from colab_app.db.schema import DSHremployeSchema


work_router = APIRouter(prefix='/predict_staff', tags=['Staff'])

model = joblib.load('colab_app/scaler_model/model_staff.pkl')
scaler = joblib.load('colab_app/scaler_model/scaler_staff.pkl')



department_list = ['Research & Development', 'Sales']
EducationField_list = ['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree']
JobRole_list = ['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director', 'Research Director', 'Research Scientist', 'Sales Executive', 'Sales Representative']
MaritalStatus_list = ['Married', 'Single']


@work_router.post('/')
async def predict(staff: DSHremployeSchema ):
    staff_dict = staff.dict()
    new_gender = staff_dict.pop('gender')
    new_overtime = staff_dict.pop('over_time')
    new_department = staff_dict.pop('department')
    new_businesst = staff_dict.pop('business_travel')
    new_education = staff_dict.pop('education_field')
    new_job_role = staff_dict.pop('job_role')
    new_marital = staff_dict.pop('marital_status')

    gender1_0 = [1 if new_gender == 'Female' else 0]
    over_time1_0 = [1 if new_overtime == 'Yes' else 0]
    business1_0 = [1 if new_businesst == 'Travel_Rarely' else 0]

    department1_0 = [1 if new_department == i else 0 for i in department_list]
    education1_0 = [1 if new_education == i else 0 for i in EducationField_list]
    job_role1_0 = [1 if new_job_role == i else 0 for i in JobRole_list]
    marital1_0 = [1 if new_marital == i else 0 for i in MaritalStatus_list]

    features = [list(staff_dict.values()) +gender1_0 +
                over_time1_0+business1_0 +department1_0
                +education1_0 + job_role1_0+marital1_0]
    scaled_data = scaler.transform(features)
    predi = model.predict(scaled_data)[0]
    if predi == 1:
        predi = 'Уйдет'
    else:
        predi = 'Останется'
    return {"predict": predi}






