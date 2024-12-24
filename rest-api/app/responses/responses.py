"""
Custom Responses
"""

from pydantic import BaseModel
from typing import Optional, Any


class CustomResponse(BaseModel):
    message: str
    response_code: int
    data: Optional[Any] = None
