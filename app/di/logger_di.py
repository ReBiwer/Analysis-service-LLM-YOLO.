import logging
from logging import Logger
from dishka import Provider, Scope, provide

from app.config import settings

class LoggerProvider(Provider):
    @provide(scope=Scope.APP)
    def get_logger_app(self) -> Logger:
        return logging.getLogger(settings.NAME_LOGGER)
