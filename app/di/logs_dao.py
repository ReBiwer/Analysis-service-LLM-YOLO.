from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao.logs import LogDAO


class LogDAOProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def get_log_dao(self, session: AsyncSession) -> LogDAO:
        return LogDAO(session)
