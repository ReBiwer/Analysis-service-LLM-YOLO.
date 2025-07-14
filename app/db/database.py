from datetime import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from app.config import settings

engine = create_async_engine(url=settings.db_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())


    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    def __repr__(self) -> str:
        """Строковое представление объекта для удобства отладки."""
        return f"<{self.__class__.__name__}(id={self.id}, created_at={self.created_at})>"
