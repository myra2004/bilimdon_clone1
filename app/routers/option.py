from fastapi import APIRouter, HTTPException, status

from app.models import *
from app.dependencies import db_dep
from app.schemas.option import *


router = APIRouter(
    prefix="/option",
    tags=["option"]
)


@router.get('/get', response_model=List[OptionGet])
async def get_questions(db: db_dep):
    return db.query(Question).all()

@router.get('/get/{id}', response_model=OptionGet)
async def get_question(id: int, db: db_dep):
    return db.query(Question).filter(Question.id == id).first()


@router.post('/create', response_model=OptionCreateResponse)
async def create_option(db: db_dep,
                        option: OptionCreate):

    option_question = db.query(Question).filter(Question.title == option.question).first()
    if not option_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question Title not found")

    db_option = Option(
        title=option.title,
        question_id=option_question.id,
        is_correct=option.is_correct,
    )

    db.add(db_option)
    db.commit()
    db.refresh(db_option)

    return db_option


@router.patch('/update/{id}', response_model=OptionUpdateResponse)
async def update_question(id:int,
                          db: db_dep,
                          option: OptionUpdate):

    option_question = db.query(Question).filter(Question.title == option.question).first()

    db_option = db.query(Question).filter(Question.id == id).first()

    if not db_option:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Option not found")

    db_option(
        title = option.title,
        description = option.description,
        question_id = option_question.id,
        updated_at = datetime.now(timezone.utc)
    )

    db.commit()
    db.refresh(db_option)

    return db_option


@router.delete('/delete/{id}', response_model=OptionGet)
async def delete_question(id: int, db: db_dep):

    db_option = db.query(Option).filter(Option.id == id).first()
    if not db_option:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Option not found")

    db.delete(db_option)
    db.commit()

    return db_option
