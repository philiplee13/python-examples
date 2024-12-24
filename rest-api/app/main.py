from fastapi import FastAPI
from resources.users import router as user_router
from auth import router as auth_router

from middleware import middleware
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()

app.include_router(user_router.router)
app.include_router(auth_router.router)
app.add_middleware(
    BaseHTTPMiddleware, dispatch=middleware.custom_middleware
)  # custom middleware
