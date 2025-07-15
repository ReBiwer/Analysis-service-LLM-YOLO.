from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BaseMessage(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )


class QueryUser(BaseMessage):
    query: str
    image_64: str


class ResponseLLM(BaseMessage):
    detected_objects: list[str]
    llm_response: str


class SchemaLogAdd(BaseMessage):
    query: str
    detected_objects: list[str]
    llm_response: str


class SchemaLog(SchemaLogAdd):
    id: int
    created_at: datetime
