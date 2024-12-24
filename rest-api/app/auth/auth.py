"""
File to handle auth
Api Key and JWT example
"""

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
import jwt
from datetime import datetime, timedelta, timezone

from fastapi import Request, status
from fastapi.responses import JSONResponse


class AuthService:
    def __init__(self):
        pass

    def validate_api_key(self, request: Request) -> bool:
        print("Validating request")
        api_key = request.headers.get("api-key", None)
        print(f"api key is {api_key}")
        if not api_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=({"message": "Missing Api Key"}),
            )
        return True

    def create_jwt(self, request: Request) -> JSONResponse:
        try:
            to_encode = {}
            expires_at: datetime = datetime.now(timezone.utc) + timedelta(minutes=1)

            # format expires_at into yyyy-mm-dd-hh-ss
            # expires_at: datetime = datetime.strptime(expires_at, "%Y-%m-%dT%H:%M:%S")
            to_encode.update({"expires_at": str(expires_at)})
            encoded_jwt = jwt.encode(
                to_encode,
                "secret",
                algorithm="HS256",
            )
            return JSONResponse(content={"token": encoded_jwt})
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(
                    {
                        "message": "Error generating JWT",
                        "request_id": request.headers["X-Request-Id"],
                        "error": str(e),
                    }
                ),
            )

    def validate_jwt(self, request: Request) -> bool:
        token = request.headers.get("authorization").split()[-1]
        decoded_jwt = jwt.decode(token, "secret", algorithms=["HS256"])
        expires_at_time = datetime.fromisoformat(decoded_jwt["expires_at"])
        now = datetime.now(timezone.utc)
        print(f"expires at {expires_at_time} vs. now time is {now}")
        print(expires_at_time < now)  # checking if the token generated was expired
        if now > expires_at_time:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=(
                    {
                        "message": "Token Expired",
                        "request_id": request.headers["X-Request-Id"],
                    }
                ),
            )
        else:
            print(f"token was not expired {token}")
            return True
