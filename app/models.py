from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, Date

from datetime import datetime, timezone, date
from typing import Optional, List

from app.db import *


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    birthdate: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    games: Mapped["Game"] = relationship('Game', back_populates='user')
    submissions: Mapped[List["Submission"]] = relationship('Submission', back_populates='user')
    participations: Mapped[List["Participation"]] = relationship('Participation', back_populates='user')


class Topic(Base):
    __tablename__ = 'topics'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    game: Mapped[List["Game"]] = relationship('Game', back_populates='topic')


class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, default='Not Information')
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey('topics.id'))
    score: Mapped[int] = mapped_column(Integer, default=0)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    user: Mapped["User"] = relationship('User', back_populates='games')
    questions: Mapped[List["GameQuestion"]] = relationship(back_populates='game')
    topic: Mapped["Topic"] = relationship('Topic', back_populates='games')
    participations: Mapped[List["Participation"]] = relationship(back_populates='game')


class GameQuestion(Base):
    __tablename__ = 'game_questions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey('questions.id'))
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey('games.id'))

    question: Mapped["Question"] = relationship(back_populates='games')
    game: Mapped["Game"] = relationship(back_populates='questions')



class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, default='Not Information')
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey('topics.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    games: Mapped[List["GameQuestion"]] = relationship(back_populates='question')
    option_ids: Mapped[List["Option"]] = relationship(back_populates='question')
    submissions: Mapped[List["Submission"]] = relationship(back_populates='question')


class Participation(Base):
    __tablename__ = 'participations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey('games.id'))
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    gained_score: Mapped[int] = mapped_column(Integer, default=0)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    user: Mapped["User"] = relationship("User", back_populates="participations")
    game: Mapped["Game"] = relationship("Game", back_populates="participations")


class Option(Base):
    __tablename__ = 'options'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey('questions.id'))
    title: Mapped[str] = mapped_column(String, unique=True)
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    question = relationship("Question", back_populates="option_ids")
    submissions: Mapped[List["Submission"]] = relationship(back_populates="option")


class Submission(Base):
    __tablename__ = 'submissions'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey('questions.id'))
    option_id: Mapped[int] = mapped_column(Integer, ForeignKey('options.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_correct:Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship("User", back_populates="submissions")
    question: Mapped["Question"] = relationship("Question", back_populates="submissions")
    option: Mapped["Option"] = relationship("Option", back_populates="submissions")


