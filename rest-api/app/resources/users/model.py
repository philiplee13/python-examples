"""
Should only be models here - class that represents db records
"""

from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
