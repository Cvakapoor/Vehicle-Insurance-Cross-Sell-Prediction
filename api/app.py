from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np

app = FastAPI()

model = mlflow.sklearn.load_model("models:/model/latest")

class CustomerFeatures(BaseModel):
    Gender: float
    Age: int
    Driving_License: int
    Region_Code: float
    Previously_Insured: int
    Vehicle_Age: float
    Vehicle_Damage: float
    Annual_Premium: float
    Policy_Sales_Channel: float
    Vintage: int

@app.post("/predict")
def predict(input: CustomerFeatures):
    features = np.array([[v for v in input.dict().values()]])
    prediction = model.predict(features)
    return {"Response": int(prediction[0])}
