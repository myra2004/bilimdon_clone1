from fastapi import APIRouter

from app.schemas.auth import *
from app.models import *
from app.dependencies import db_dep
from app.utils import *


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post('/registration', response_model=AuthRegistraionResponse)
def registration(db: db_dep,
                 user: AuthRegistration):
    db_user = User(
        email = user.email,
        username = user.username,
        password = hash_password(user.password),
        first_name = user.first_name,
        last_name = user.last_name,
        birthdate=user.birthdate,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user