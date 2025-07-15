from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Query

from app.db.repositories.logs import LogRepository
from app.schemas.messages import QueryUser, ResponseLLM, SchemaLog
from app.use_cases.analyze_img import AnalyzeImgUseCase

router = APIRouter(
    tags=["yolo-analyze"],
    prefix="/yolo",
    route_class=DishkaRoute
)


@router.post('/analyze')
async def analyze_img(
        query: QueryUser,
        use_cases: FromDishka[AnalyzeImgUseCase],
) -> ResponseLLM:
    response = await use_cases.analyze(query)
    return response


@router.get('/logs')
async def get_logs(
        log_dao: FromDishka[LogRepository],
        count_record: Annotated[int, Query()] = 10,
) -> list[SchemaLog]:
    records = await log_dao.find_all(count_record)
    results = [SchemaLog.model_validate(record) for record in records]
    return results
