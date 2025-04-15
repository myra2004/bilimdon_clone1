from pydantic import BaseModel

from typing import Optional
from datetime import datetime, timezone


class GameResponse(BaseModel):
    id: int
    owner_id: int | 1
    title: str
    description: Optional[str] = 'Not Information'
    topic_id: int
    score: int | 0
    start_time: datetime
    end_time: datetime



class GameCreate(BaseModel):
    title: str
    description: Optional[str] = 'Not Information'
    topic: Optional[str]
    score: int | 0
    start_time: datetime
    end_time: datetime


class GameUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str] = 'Not Information'
    topic: Optional[str]
    score: Optional[int]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
