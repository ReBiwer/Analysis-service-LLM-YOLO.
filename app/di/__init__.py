from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka as fastapi_dishka
from fastapi import FastAPI

from app.di.db_session import DBSessionProvider
from app.di.llm import LLMServiceProvider
from app.di.logger_di import LoggerProvider
from app.di.logs_dao import LogDAOProvider
from app.di.yolo import YOLOServiceProvider


def init_di_web(app: FastAPI) -> None:
    container = container_factory()
    fastapi_dishka(container, app)


def container_factory() -> AsyncContainer:
    return make_async_container(
        DBSessionProvider(),
        LogDAOProvider(),
        LoggerProvider(),
        LLMServiceProvider(),
        YOLOServiceProvider(),
    )
