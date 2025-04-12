from fastapi import APIRouter, Depends

from app.models import User
from app.dependencies import db_dep

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get('/get')
async def grt(db: db_dep):
    return db.query(User).all()