from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
import uuid
from auth.auth import AuthService

auth_service = AuthService()


async def custom_middleware(request: Request, call_next):
    print("inside middleware")
    request_id = uuid.uuid4()
    new_headers = request.headers.mutablecopy()
    new_headers.append("X-Request-Id", str(request_id))
    request._headers = new_headers
    request.scope.update(headers=request.headers.raw)

    response = await call_next(request)

    response.headers["X-Request-Id"] = str(request_id)
    return response
