from fastapi import FastAPI, Query, APIRouter, Request, HTTPException

from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from typing import Any
from pydantic import BaseModel,ValidationError
import pickle
import numpy as np
import uvicorn
import os

api_router = APIRouter()

file = os.getcwd() + "/app_heart/heart_model.pkl"
model = pickle.load(open(file, "rb"))

class input(BaseModel):
    age : float
    sex : float
    cp : float
    trestbps : float
    chol : float
    fbs : float
    restecg : float
    thalach : float
    exang : float
    oldpeak : float
    slope : float
    ca : float
    thal : float


class output(BaseModel):
    prediction : int

@api_router.on_event("startup")
def load_model():
    pass


@api_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the heart Disease API</h1>"
        "<p> </p>"
        "<h2>it's working ! </h2>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )


    return HTMLResponse(content=body)

@api_router.post('/predict/')
def predict(message: input):
    print(file)
    values = [v for v in message.__dict__.values()]
    prediction_result = model.predict(np.array([values]).reshape(1, -1))[0]
    return 200,output(prediction=prediction_result)

if __name__ == "__main__":
    uvicorn.run("index:api_router", reload=True)
