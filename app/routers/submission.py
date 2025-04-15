from fastapi import APIRouter, HTTPException, status

from typing import List

from app.dependencies import db_dep
from app.models import *
from app.schemas.submission import *


router = APIRouter(prefix="/submission", tags=["submission"])


@router.get("/", response_model=List[SubmissionResponse])
async def get_all_submissions(db: db_dep):
    return db.query(Submission).all()


@router.get("/{id}/", response_model=SubmissionResponse)
async def get_submission_by_id(id: int, db: db_dep):
    return db.query(Submission).filter(Submission.id == id).first()


@router.post("/create/", response_model=SubmissionResponse)
async def create_submission(db: db_dep,
                            submission: SubCreate):
    db_submission = Submission(
        question_id=submission.question_id,
        option_id=submission.option_id,
        is_correct=submission.is_correct,
    )

    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)

    return db_submission


@router.patch("/{id}/", response_model=SubmissionResponse)
async def update_submission(db: db_dep,
                            submission: SubUpdate):
    db_submission = db.query(Submission).filter(Submission.id == submission.id).first()

    if not db_submission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Submission not found")

    db_submission.question_id = submission.question_id
    db_submission.option_id = submission.option_id
    db_submission.is_correct = submission.is_correct

    db.commit()
    db.refresh(db_submission)
    return db_submission


@router.delete("/{id}/", response_model=SubmissionResponse)
async def update_submission(db: db_dep,
                            submission: SubUpdate):
    db_submission = db.query(Submission).filter(Submission.id == submission.id).first()

    if not db_submission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Submission not found")

    db.delete(db_submission)
    db.commit()
    return db_submission
