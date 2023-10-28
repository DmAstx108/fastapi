from fastapi import FastAPI

from .tgbot import launch

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.operations.router_research import router1 as router_operation1
from src.operations.router_question import router2 as router_operation2
from src.tasks.router import router as router_operation3

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

app = FastAPI(
    title="Опросы"
)


def tgbot_launching(app, launch):
    if app:
        return launch
    else:
        print('something is bad!')


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


app.include_router(router_operation1)
app.include_router(router_operation2)
app.include_router(router_operation3)

tgbot_launching(app, launch)
