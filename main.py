from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')


diabets_app = FastAPI()

class DiabetsSchema(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int



@diabets_app.post('/predict', response_model=dict)
async def predict_bank(deabet: DiabetsSchema):
    diabets_data = deabet.dict()


    data = list(diabets_data.values())

    scaled_data = scaler.transform([data])
    pred = model.predict(scaled_data)[0]
    new_data = 'Diabets' if pred == 1 else 'No'
    return {'Predict': new_data}

if __name__ == '__main__':
    uvicorn.run(diabets_app, host='127.0.0.1', port=8008)