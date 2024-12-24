"""
api routes
"""

from fastapi import APIRouter, Depends, Request
from resources.users.service import UserService
from resources.users.model import UserModel
from auth.auth import AuthService

router = APIRouter(prefix="/users")
service = UserService()
auth_service = AuthService()


@router.get("/", dependencies=[Depends(auth_service.validate_api_key)])
def get_all_users(request: Request):
    print(f"request id is {request.headers['X-Request-Id']}")
    return service.get_all_users()


@router.post("/", dependencies=[Depends(auth_service.validate_api_key)])
def create_user(request: Request, user: UserModel):
    print(f"request id is {request.headers['X-Request-Id']}")
    return service.create_user(user)


@router.delete("/{user_id}", dependencies=[Depends(auth_service.validate_api_key)])
def delete_user(request: Request, user_id: int):
    return service.delete_user(user_id=user_id)


@router.put("/{user_id}", dependencies=[Depends(auth_service.validate_api_key)])
def update_user(request: Request, user_id: int, user_to_update: UserModel):
    return service.update_user(user_id=user_id, user_to_update=user_to_update)
