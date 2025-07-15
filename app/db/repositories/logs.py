import logging
from typing import Sequence

from sqlalchemy import desc, insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.domain.entities.logs import LogEntity, LogInfo
from app.domain.repositories.logs import AbstractLogsRepository
from app.models.logs import Log as LogModel

logger = logging.getLogger(settings.NAME_LOGGER)


class LogRepository(AbstractLogsRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, log_data: LogEntity) -> None:
        try:
            stmt = insert(LogModel).values(**log_data.model_dump())
            await self._session.execute(stmt)
            logger.info("Лог успешно добавлен в базу данных.")
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при добавлении лога: {e}")
            raise

    async def find_all(self, limit: int = 10, offset: int = 0) -> Sequence[LogInfo]:
        logger.info(f"Получение {limit} записей с отступом {offset}")
        try:
            query = select(LogModel).order_by(desc(LogModel.created_at)).limit(limit).offset(offset)
            result = await self._session.execute(query)
            records = result.scalars().all()
            logger.info(f"Найдено {len(records)} записей.")
            return [LogInfo.model_validate(record) for record in records]
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при получении записей: {e}")
            raise
