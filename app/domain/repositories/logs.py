from abc import ABC, abstractmethod
from typing import Sequence

from app.domain.entities.logs import Log


class AbstractLogsRepository(ABC):
    @abstractmethod
    async def add(self, log_data: Log) -> None:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, limit: int = 100, offset: int = 0) -> Sequence[Log]:
        raise NotImplementedError 