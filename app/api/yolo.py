from typing import Annotated, Sequence

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Query

from app.domain.repositories.logs import AbstractLogsRepository
from app.domain.entities.logs import LogInfo
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
        log_repo: FromDishka[AbstractLogsRepository],
        count_record: Annotated[int, Query()] = 10,
) -> Sequence[LogInfo]:
    records = await log_repo.find_all(count_record)
    return records
