from datetime import datetime
from pydantic import BaseModel, ConfigDict


class LogEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    query: str
    detected_objects: list[str]
    llm_response: str

class LogInfo(LogEntity):
    id: int
    created_at: datetime