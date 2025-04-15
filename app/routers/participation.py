from fastapi import APIRouter,  HTTPException, status

from typing import List

from app.schemas import QuestionGet
from app.schemas.participation import *
from app.models import *
from app.dependencies import db_dep


router = APIRouter(prefix="/participation", tags=["participation"])


@router.get('/', response_model=ParticipationResponse)
async def participation_get(db: db_dep):
    return db.query(Participation).all()


@router.get('/{id}', response_model=ParticipationResponse)
async def participation_get_id(id: int, db: db_dep):
    return db.query(Participation).filter(Participation.id == id).first()


@router.post('/create/', response_model=ParticipationResponse)
async def participation_create(db: db_dep, participation: ParticipationResponse):
    pass
# participationda user kirib uynaydi, userni kimligi va uni boshlagan tugagan vaqti va qancha score yigilganligi saqlanib qolish kere
