from fastapi import Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt

from typing import Annotated
from datetime import timedelta, datetime, timezone

from app.db import *
from app.utils import *
from app.models.user import User


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dep = Annotated[Session, Depends(get_db)]


def get_current_user(
        request:Request,
        db: db_dep
):
    auth_header = request.headers.get("Authorization")
    is_bearer = auth_header.startswith("Bearer") if auth_header else False
    token = auth_header.split(" ")[1] if auth_header else " "

    if not auth_header and is_bearer:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authorized'
        )

    try:
        decoded_jwt = jwt.decode(
            SECRET_KEY,
            ALGORITHM,
            token
        )

        print(decoded_jwt)
        email = decoded_jwt["email"]
        password = decoded_jwt["password"]
        db_user = db.query(User).filter(User.email == email).first()

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Token'
        )

    return db_user


def get_superuser(
        user: User = Depends(get_current_user)
):
    if not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='User has not permission'
        )

    return user


def get_staff(
        user: User = Depends(get_current_user)
):
    if not user.is_staff:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='User has not permission'
        )

    return user


current_user_dep = Annotated[User, Depends(get_current_user)]
superuser_dep = Annotated[User, Depends(get_superuser)]
staff_dep = Annotated[User, Depends(get_staff)]