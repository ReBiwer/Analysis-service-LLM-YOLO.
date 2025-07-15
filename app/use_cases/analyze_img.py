from app.schemas.messages import QueryUser, ResponseLLM
from app.services.yolo import YOLOService
from app.services.llm import LLMService
from app.db.dao.logs import LogDAO


class AnalyzeImgUseCase:

    def __init__(
            self,
            yolo_service: YOLOService,
            llm_service: LLMService,
            dao: LogDAO,
    ):
        self.yolo_service = yolo_service
        self.llm_service = llm_service
        self.dao = dao

    async def analyze(self, query: QueryUser) -> ResponseLLM:
        objects = self.yolo_service.detect_image(query.image_64)
        llm_response = self.llm_service.get_response(query.query, objects)
        response = ResponseLLM(detected_objects=objects, llm_response=llm_response)
        await self.dao.add(response)
        return response
