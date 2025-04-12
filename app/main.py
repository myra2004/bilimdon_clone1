from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.question import router as question_router
from app.routers.option import router as option_router
from app.routers.topic import router as topic_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(topic_router)
app.include_router(question_router)
app.include_router(option_router)