from fastapi import APIRouter, HTTPException, status

users_router = APIRouter(tags=["Users"])


@users_router.get("/me")
async def get_user_info():
    return {"message": "User info"}


@users_router.get("/{id}")
async def filter_user_by_id(id: int):
    return {"message": f"user id: {id}"}

