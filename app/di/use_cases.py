from dishka import Provider, provide, Scope

from app.services.llm import LLMService
from app.services.yolo import YOLOService
from app.db.dao.logs import LogDAO
from app.use_cases.analyze_img import AnalyzeImgUseCase


class AnalyzeImgUCProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def get_use_case(
            self,
            llm_service: LLMService,
            yolo_service: YOLOService,
            dao: LogDAO
    ) -> AnalyzeImgUseCase:
        return AnalyzeImgUseCase(
            llm_service=llm_service,
            yolo_service=yolo_service,
            dao=dao
        )
