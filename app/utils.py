from passlib.context import CryptContext
from jose import jwt

from datetime import timedelta, timezone, datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


ALGORITHM = "HS256"
SECRET_KEY = 'void@pointer'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 1800


def create_access_token(data: dict, expires_delta: float = None):
    delta = timedelta(minutes=expires_delta) if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire_time = datetime.now(timezone.utc) + delta
    data.update({'exp': expire_time})

    access_token = jwt.encode(
        data,
        SECRET_KEY,
        ALGORITHM
    )

    return access_token