from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# # Load your pre-trained model
# with open("model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# # Pydantic model for input validation
# class InputData(BaseModel):
#     features: list[float]

@app.get("/")
async def root():
    return {"message": "Welcome to the prediction API!"}

# @app.post("/predict/")
# async def predict(input_data: InputData):
#     # Ensure input is a 2D array
#     input_array = np.array([input_data.features])

#     # Run model prediction
#     prediction = model.predict(input_array)
#     return {"prediction": prediction.tolist()}
