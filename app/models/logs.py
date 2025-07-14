from sqlalchemy import JSON, Column
from sqlalchemy.orm import Mapped

from app.db.database import Base


class Log(Base):
    query: Mapped[str]
    detected_objects = Column(JSON)
    llm_response: Mapped[str]
