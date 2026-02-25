from pydantic import BaseModel


class TelecomSchema(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    PaperlessBilling: str
    MonthlyCharges: float
    TotalCharges: float
    PaymentMethod: str
    Contract: str
    InternetService: str
    MultipleLines: str

class MashSchema(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str
    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str
    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str
    veil_type: str
    veil_color: str
    ring_number: str
    ring_type: str
    spore_print_color: str
    population: str
    habitat: str


class HousePredictSchema(BaseModel):
    GrLivArea: int
    YearBuilt: int
    GarageCars: int
    TotalBsmtSF: int
    FullBat: int
    OverallQual: int
    Neighborhood: str


class DiabetSchema(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

class TitanicSchema(BaseModel):
    Embarked: str
    Fare: float
    Parch: int
    SibSp: int
    Age: float
    Sex: str
    Pclass: int


class BankPredict1Schema(BaseModel):
    person_age: float
    person_gender: str
    person_education: str
    person_income: float
    person_emp_exp: int
    person_home_ownership: str
    loan_amnt: float
    loan_intent: str
    loan_int_rate: float
    credit_score: int
    loan_percent_income: float
    cb_person_cred_hist_length: float
    previous_loan_defaults_on_file: str

class AvocadoSchema(BaseModel):
    firmness: float
    hue: int
    saturation: int
    brightness: int
    color_category: str
    sound_db: int
    weight_g: int
    size_cm3: int

class StudentSchema(BaseModel):
    reading_score: int
    writing_score: int
    gender_male: str
    race_ethncity: str
    parental: str
    level: str
    parental_level: str
    lunch: str
    test: str