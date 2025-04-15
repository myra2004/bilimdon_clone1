from pydantic import BaseModel

from typing import Optional
from datetime import datetime, timezone


class ParticipationResponse(BaseModel):
    id: int
    user_id: int | 1
    game_id: int
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    gained_score: int | 0
    registered_at: Optional[datetime] = datetime.now(timezone.utc)


