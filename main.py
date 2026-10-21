from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.post("/predict", summary="Predict purchase probability")
async def predict(data: dict):
    """Receives customer data and returns purchase probability"""
    prediction = np.random.choice([0, 1])  
    return {"prediction": int(prediction)}