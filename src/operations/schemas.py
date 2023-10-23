from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str


class Research(BaseModel):
    id: int
    title: str
    total_question: int
    start_date: datetime
    finish_date: datetime
    question_id: int


class ResearchCreate(BaseModel):
    id: int
    title: str
    total_question: int
    start_date: datetime
    finish_date: datetime
    question_id: int


class QuestionCreate(BaseModel):
    id: int
    title: str
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    answer5: str


class Question(BaseModel):
    id: int
    title: str
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    answer5: str
