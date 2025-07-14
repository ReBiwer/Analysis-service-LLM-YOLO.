from logging import Logger
from dishka import Provider, Scope, provide

from app.services.yolo import YOLOService


class YOLOServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_yolo_service(self, logger: Logger) -> YOLOService:
        return YOLOService(logger)
