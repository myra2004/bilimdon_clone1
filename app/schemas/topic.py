from pydantic import BaseModel


class TopicGet(BaseModel):
    id: int
    name: str


class TopicCreate(BaseModel):
    name: str

class TopicCreateResponse(TopicCreate):
    id:int