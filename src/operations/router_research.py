import time

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache
from src.database import get_async_session
from src.operations.models import research
from src.operations.schemas import ResearchCreate

router1 = APIRouter(
    prefix="/researches",
    tags=["Research"],
)


@router1.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router1.get("/")
async def get_specific_operations(research_title: str, session: AsyncSession = Depends(get_async_session)):
    query = select(research).where(research.c.title == research_title)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]

# @router1.get("/id")
# async def get_research_by_id(research_title: str, session: AsyncSession = Depends(get_async_session)):
#     query = select(research).where(research.c.title == research_title)
#     result = await session.execute(query)
#     return [dict(r._mapping) for r in result]


@router1.post("/")
async def add_specific_operations(new_research: ResearchCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(research).values(**new_research.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
