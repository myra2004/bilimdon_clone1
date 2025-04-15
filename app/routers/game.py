from fastapi import APIRouter, HTTPException, status

from typing import List

from app.models import *
from app.dependencies import db_dep
from app.schemas import *


router = APIRouter(prefix="/game", tags=["game"])


@router.get("/", response_model=List[GameResponse])
async def get_games(db: db_dep):
    return db.query(Game).all()


@router.get("/{id}", response_model=GameResponse)
async def get_game(id: int, db: db_dep):
    return db.query(Game).filter(Game.id == id).first()


@router.post("/", response_model=GameResponse)
async def create_game(db: db_dep,
                      game: GameCreate):
    game_topic = db.query(Topic).filter(Topic.name == game.topic).first()

    if not game_topic:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='topic not found')

    db_game = Game(
        title=game.title,
        description=game.description,
        topic_id = game_topic.id,
        score=game.score,
        start_time=game.start_time,
        end_time=game.end_time,
    )

    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


@router.patch("/{id}", response_model=GameResponse)
async def update_game(id: int,
                      db: db_dep,
                      game: GameUpdate):
    game_topic = db.query(Topic).filter(Topic.name == game.topic).first()

    db_game = db.query(Game).filter(Game.id == id).first()

    if not db_game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='game not found')

    db_game.title = game.title
    db_game.description = game.description
    db_game.topic_id = game_topic.id
    db_game.score = game.score
    db_game.start_time = game.start_time
    db_game.end_time = game.end_time

    db.commit()
    db.refresh(db_game)
    return db_game


@router.delete('/delete/{id}', response_model=GameResponse)
async def delete_game(id: int, db: db_dep):

    db_game = db.query(Game).filter(Game.id == id).first()
    if not db_game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found")

    db.delete(db_game)
    db.commit()

    return db_game


