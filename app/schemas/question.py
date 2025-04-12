from pydantic import BaseModel

from typing import Optional
from datetime import datetime, timezone

from app.models import Question


class QuestionGet(BaseModel):
    id: int
    title: str
    description: Optional[str] = 'Not Information'
    topic_id: int
    created: Optional[datetime] = datetime.now(timezone.utc)
    updated: Optional[datetime] = datetime.now(timezone.utc)


class QuestionCreate(BaseModel):
    title: str
    description: Optional[str] = 'Not Information'
    topic: Optional[str] = 'Not Information'


class QuestionCreateResponse(QuestionCreate):
    pass


class QuestionUpdate(BaseModel):
    title: Optional[str] = Question.title
    description: Optional[str] = Question.description
    topic: Optional[str]


class QuestionUpdateResponse(QuestionUpdate):
    updated: Optional[datetime] = datetime.now(timezone.utc)
