"""
api routes for auth
"""

from fastapi import APIRouter, Request
from auth.auth import AuthService

router = APIRouter(prefix="/auth")
service = AuthService()


@router.post("/")
def create_access_token(request: Request):
    print("inside auth router - creating jwt")
    return service.create_jwt(request)


@router.get("/validate")
def validate_access_token(request: Request):
    return service.validate_jwt(request)
