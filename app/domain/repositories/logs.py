from abc import ABC, abstractmethod
from collections.abc import Sequence

from app.domain.entities.logs import LogEntity, LogInfo


class AbstractLogsRepository(ABC):
    @abstractmethod
    async def add(self, log_data: LogEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, limit: int = 10, offset: int = 0) -> Sequence[LogInfo]:
        raise NotImplementedError
