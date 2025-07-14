from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseMessage(BaseModel):
    query: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class QueryUser(BaseMessage):
    image_64: str


class ResponseLLM(BaseMessage):
    detected_objects: list[str]
    llm_response: str


class SchemaLog(ResponseLLM):
    id: int
    created_at: datetime
