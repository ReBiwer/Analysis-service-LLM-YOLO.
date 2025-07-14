import logging
import logging.config
import os

from app.config import settings

LOG_DIR = settings.BASE_DIR / "logs/backend"


def setup_logging() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            settings.NAME_LOGGER: {
                "level": "DEBUG",
                "handlers": ["console"],
            },
        },
    }

    logging.config.dictConfig(logging_config)
