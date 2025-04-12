from pydantic import BaseModel

from datetime import datetime,  timezone
from typing import Optional

from app.models import Option


class OptionGet(BaseModel):
    id: int
    title: str
    question_id: int
    is_correct: bool = False
    created_at: Optional[datetime] = datetime.now(timezone.utc)


class OptionCreate(BaseModel):
    title: str
    question: Optional[str]
    is_correct: bool = False

class OptionCreateResponse(OptionCreate):
    id: int
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    question_id: int


class OptionUpdate(BaseModel):
    title: Optional[str] = Option.title
    question: Optional[str]
    is_correct: Optional[bool] = Option.is_correct


class OptionUpdateResponse(OptionUpdate):
    id: int