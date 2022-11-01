import json
import requests
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn


class InputItems(BaseModel):
    furniture_type: int = Field(..., description="0: unknown, 1: full, 2: cơ bản, 3: full cao cấp, 4: nguyên bản")
    apartment_type: int = Field(..., description="0: tập thể, 1: thường, 2: studio, 3: mini, 4: cao cấp")
    news_type: int = Field(..., description='0: môi giới, 1: cá nhân')
    bedroom_number: int
    area: float
    latitude: float
    longitude: float


app = FastAPI(title='Capstone API', version='0.1.0')
model = joblib.load('../model/best_random_forest.joblib')


@app.post("/predict")
async def predict_price(item: InputItems):

    data_point = np.array([item.news_type, item.bedroom_number,
                           item.area, item.apartment_type, item.furniture_type,
                           item.latitude, item.longitude])

    price = model.predict(data_point.reshape(1, -1))
    price = price[0]
    price = round(price, 1)
    print(price)

    return {'price': price}


if __name__ == '__main__':
    uvicorn.run(app, port=8004)
