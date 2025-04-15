from fastapi import APIRouter, HTTPException, status

from typing import List

from app.schemas.question import *
from app.dependencies import db_dep
from app.models import *


router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get('/get', response_model=List[QuestionGet])
async def get_questions(db: db_dep):
    return db.query(Question).all()

@router.get('/get/{id}', response_model=QuestionGet)
async def get_question(id: int, db: db_dep):
    return db.query(Question).filter(Question.id == id).first()


@router.post('/create', response_model=QuestionCreateResponse)
async def create_question(db: db_dep,
                          question: QuestionCreate):

    question_topic = db.query(Topic).filter(Topic.name == question.topic).first()
    if not question_topic:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found")

    db_question = Question(
        title = question.title,
        description = question.description,
        topic_id = question_topic.id,
        owner_id=2,
        created_at = datetime.now(timezone.utc),
    )

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


@router.patch('/update/{id}', response_model=QuestionUpdateResponse)
async def update_question(id:int,
                          db: db_dep,
                          question: QuestionUpdate):

    question_topic = db.query(Topic).filter(Topic.name == question.topic).first()

    db_question = db.query(Question).filter(Question.id == id).first()

    if not db_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    db_question.title = question.title
    db_question.description = question.description
    db_question.topic_id = question_topic.id
    db_question.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_question)

    return db_question


@router.delete('/delete/{id}', response_model=QuestionGet)
async def delete_question(id: int, db: db_dep):

    db_question = db.query(Question).filter(Question.id == id).first()
    if not db_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    db.delete(db_question)
    db.commit()

    return db_question
