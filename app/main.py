import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager, AbstractAsyncContextManager

from app.di import init_di_web
from app.api import yolo
from app.log_settings import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Telegram AI Assistant Backend",
        description="Backend for handling AI requests from Telegram bot.",
        lifespan=lifespan,
    )
    app.include_router(yolo.router)
    init_di_web(app)
    setup_logging()
    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", host='0.0.0.0', port=8000, reload=True)
