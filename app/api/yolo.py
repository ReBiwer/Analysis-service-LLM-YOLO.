from fastapi import APIRouter, Query
from typing import Annotated
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute

from app.schemas.messages import QueryUser, ResponseLLM, SchemaLog
from app.services.yolo import YOLOService
from app.services.llm import LLMService
from app.db.dao.logs import LogDAO


router = APIRouter(
    tags=["yolo-analyze"],
    prefix="/yolo",
    route_class=DishkaRoute
)


@router.post('/analyze')
async def analyze_img(
        query: QueryUser,
        yolo_service: FromDishka[YOLOService],
        llm_service: FromDishka[LLMService],
        log_dao: FromDishka[LogDAO],
) -> ResponseLLM:
    objects = yolo_service.detect_image(query.image_64)
    llm_response = llm_service.get_response(query.query, objects)
    response = ResponseLLM(query=query.query, detected_objects=objects, llm_response=llm_response)
    await log_dao.add(response)
    return response


@router.get('/logs')
async def get_logs(
        log_dao: FromDishka[LogDAO],
        count_record: Annotated[int, Query()] = 10,
) -> list[SchemaLog]:
    records = await log_dao.find_all(count_record)
    results = [SchemaLog.model_validate(record) for record in records]
    return results
