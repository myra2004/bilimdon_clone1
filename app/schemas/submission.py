from pydantic import BaseModel

from typing import Optional
from datetime import datetime, timezone


class SubmissionResponse(BaseModel):
    id: int
    user_id: int
    question_id: int
    option_id: int
    is_correct: bool | False
    created_at: Optional[datetime] = datetime.now(timezone.utc)


class SubCreate(BaseModel):
    is_correct: bool
    question_id: int
    option_id: int


class SubUpdate(BaseModel):
    is_correct: Optional[bool]
    question_id: Optional[int]
    option_id: Optional[int]