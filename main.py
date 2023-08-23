from fastapi import FastAPI
import uvicorn
from routes.cars import car_router

app = FastAPI()
app.include_router(car_router, prefix="/car")


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)