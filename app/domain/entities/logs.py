from typing import Any

from pydantic import BaseModel, ConfigDict


class Log(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    query: str
    detected_objects: list[dict[str, Any]]
    llm_response: str 