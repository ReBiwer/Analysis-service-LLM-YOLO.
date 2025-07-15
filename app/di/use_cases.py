from dishka import Provider, Scope, provide

from app.domain.repositories.logs import AbstractLogsRepository
from app.services.llm import LLMService
from app.services.yolo import YOLOService
from app.use_cases.analyze_img import AnalyzeImgUseCase


class AnalyzeImgUCProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def get_use_case(
        self,
        llm_service: LLMService,
        yolo_service: YOLOService,
        dao: AbstractLogsRepository,
    ) -> AnalyzeImgUseCase:
        return AnalyzeImgUseCase(
            llm_service=llm_service, yolo_service=yolo_service, repo=dao
        )
