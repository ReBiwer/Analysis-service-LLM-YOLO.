from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str
    PROXY_URL: str
    OPENAI_API_KEY: str
    NAME_LOGGER: str = "yolo_service"

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:5432/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=f"/{BASE_DIR}/.env")

settings = Settings()
