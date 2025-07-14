from logging import Logger
from dishka import Provider, Scope, provide

from app.services.llm import LLMService


class LLMServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_yolo_service(self, logger: Logger) -> LLMService:
        return LLMService(logger)
