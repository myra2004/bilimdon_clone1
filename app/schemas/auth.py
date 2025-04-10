from pydantic import BaseModel, Field

from typing import Optional
from datetime import date, datetime, timezone


class AuthRegistration(BaseModel):
    email: str
    password: str
    username: str
    first_name: str
    last_name: str
    birthdate: Optional[date] = None


class AuthRegistraionResponse(BaseModel):
    id: int
    joined_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: Optional[bool] = True
    is_staff: Optional[bool] = False
    is_superuser: Optional[bool] = False

    model_config= {
        "arbitrary_types_allowed": True,
    }