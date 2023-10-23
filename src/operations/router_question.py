import time
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache
from src.database import get_async_session
from src.operations.models import question
from src.operations.schemas import Question, QuestionCreate

router2 = APIRouter(
    prefix="/questions",
    tags=["Question"],
)


@router2.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись 200 лет"


@router2.get("/")
async def get_specific_operations(question_title: str, session: AsyncSession = Depends(get_async_session)):
    query = question.select().where(question.c.title == question_title)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]


@router2.post("/")
async def add_specific_operations(new_question: QuestionCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(question).values(**new_question.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
