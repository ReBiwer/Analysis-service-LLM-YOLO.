from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.logs import LogRepository
from app.domain.repositories.logs import AbstractLogsRepository


class LogDAOProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def get_log_dao(self, session: AsyncSession) -> AbstractLogsRepository:
        return LogRepository(session)
