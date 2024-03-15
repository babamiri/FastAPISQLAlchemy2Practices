import logging
import os
from typing import Optional

from dotenv import load_dotenv
load_dotenv()
DATABASE_URL_ENV = os.environ.get("DATABASE_URL")

# from pydantic_settings import BaseSettings,PostgresDsn
from pydantic import BaseModel as BaseSettings, PostgresDsn

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    """App settings."""

    project_name: str = "FastAPI SQLAlchemy2 Practices"
    debug: bool = False
    environment: str = "local"

    # Database
    # database_url: str = ""

    DATABASE_URL: Optional[
        PostgresDsn
    ] = DATABASE_URL_ENV
    DB_ECHO_LOG: bool = False

    @property
    def async_database_url(self) -> Optional[str]:
        return (
            self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            if self.DATABASE_URL
            else self.DATABASE_URL
        )


settings = Settings()