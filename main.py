from fastapi import FastAPI
import uvicorn
from routes.cars import cars_router
from routes.users import users_router

app = FastAPI()
app.include_router(cars_router, prefix="/cars")
app.include_router(users_router, prefix="/users")


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)