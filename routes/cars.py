from fastapi import APIRouter, HTTPException, status
from models.cars import Car

car_router = APIRouter(tags=["Car"])


@car_router.get("/")
async def car_list() -> dict:
    car = Car(
        brand="Lancia",
        make="Musa",
        fuel="PETROL",
        year="2006",
        countries=["Italy", "France"])
    return {"message": "car list"}


