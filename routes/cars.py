from fastapi import APIRouter, HTTPException, status
from models.cars import Car

cars_router = APIRouter(tags=["Cars"])


@cars_router.get("/")
async def car_list() -> dict:
    car = Car(
        brand="Lancia",
        make="Musa",
        fuel="PETROL",
        year="2006",
        countries=["Italy", "France"])
    print(car.model_dump_json())
    return {"message": "car list"}


@cars_router.get("/{id}")
async def filter_by_id(id: int):
    return {"message": f"car_id: {id}"}


@cars_router.post("/")
async def create_new_car():
    return {"message": "Post request success"}


