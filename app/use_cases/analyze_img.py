from app.domain.entities.logs import Log as LogEntity
from app.domain.repositories.logs import AbstractLogsRepository
from app.schemas.messages import QueryUser, ResponseLLM
from app.services.llm import LLMService
from app.services.yolo import YOLOService


class AnalyzeImgUseCase:
    def __init__(
        self,
        yolo_service: YOLOService,
        llm_service: LLMService,
        repo: AbstractLogsRepository,
    ):
        self.yolo_service = yolo_service
        self.llm_service = llm_service
        self.repo = repo

    async def analyze(self, query: QueryUser) -> ResponseLLM:
        objects = self.yolo_service.detect_image(query.image_64)
        llm_response_text = self.llm_service.get_response(query.query, objects)

        log_entry = LogEntity(
            query=query.query,
            detected_objects=objects,
            llm_response=llm_response_text,
        )
        await self.repo.add(log_entry)

        return ResponseLLM(
            detected_objects=objects, llm_response=llm_response_text
        )
