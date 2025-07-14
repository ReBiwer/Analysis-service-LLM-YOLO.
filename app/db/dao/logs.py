import logging
from sqlalchemy import desc, select
from sqlalchemy.exc import SQLAlchemyError

from app.db.dao.base import BaseDAO
from app.models.logs import Log
from app.config import settings

logger = logging.getLogger(settings.NAME_LOGGER)

class LogDAO(BaseDAO):
    model = Log

    async def find_all(self, count: int = 10):
        logger.info(f"Получаем {count} записей, отфильтрованных по полю created_at")
        try:
            query = select(self.model).order_by(desc(self.model.created_at)).limit(count)
            result = await self._session.execute(query)
            records = result.scalars().all()
            logger.info(f"Найдено {len(records)} записей")
            return records
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при получении записей: {e}")
            raise
