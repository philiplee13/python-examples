"""
api routes
"""

from fastapi import APIRouter
from services import user_service
from models import user_model

router = APIRouter(prefix="/users")
service = user_service.UserService()


@router.get("/")
def get_all_users():
    print("inside of get route")
    return service.get_all_users()


@router.post("/")
def create_user(user: user_model.UserModel):
    print("inside of create methjod", user)
    return service.create_user(user)


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return service.delete_user(user_id=user_id)


@router.put("/{user_id}")
def update_user(user_id: int, user_to_update: user_model.UserModel):
    return service.update_user(user_id=user_id, user_to_update=user_to_update)
