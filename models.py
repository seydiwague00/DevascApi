from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel

class Gender(str, Enum):
    male = "Male"
    female = "Female"

class Role(str, Enum):
    admin = "Admin"
    user = "User"
    student = "Student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]

    class Config:
        arbitrary_types_allowed = True