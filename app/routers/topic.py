from fastapi import APIRouter, HTTPException, status

from app.schemas.topic import *
from app.dependencies import db_dep
from app.models import *


router = APIRouter()

@router.get('/get', response_model=List[TopicGet])
def get_topics(db: db_dep):
    return db.query(Topic).all()


@router.post('/create', response_model=TopicCreateResponse)
def create_topic(db: db_dep,
                 topic: TopicCreate):

    db_topic = Topic(name=topic.name)

    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)

    return db_topic


@router.delete('/delete/{id}', response_model=TopicGet)
def delete_topic(db: db_dep, id: int):
    db_topic = db.query(Topic).filter(Topic.id == id).first()

    db.delete(db_topic)
    db.commit()

    return db_topic