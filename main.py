from typing import List
from fastapi import FastAPI
import uvicorn
from models.car import Car


app = FastAPI()


@app.get("/")
async def home():
    car = Car(
        brand="Lancia",
        model="Musa",
        fuel="PETROL",
        year="2006",
        countries=["Italy", "France"]
    )
    return {"message": "Welcome to FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)