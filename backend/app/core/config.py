"""Module to hold config."""
from functools import lru_cache
import secrets
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import AnyHttpUrl
from pydantic import BaseSettings
from pydantic import PostgresDsn
from pydantic import validator


class Settings(BaseSettings):
    """App settings, mapped from environment variables."""

    secret_key: str = secrets.token_urlsafe(32)
    backend_cors_origins: List[AnyHttpUrl] = []

    @validator("backend_cors_origins", pre=True)
    def assemble_cors_origins(
        cls, value: Union[str, List[str]]  # noqa: N805,B902
    ) -> Union[List[str], str]:
        """Validated the `backend_cors_origins` setting."""
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]
        if isinstance(value, (list, str)):
            return value
        raise ValueError(value)

    project_name: str = "infilmation"

    postgres_server: str = "localhost"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "infilmation"
    postgres_port: Optional[str] = "5432"
    sqlalchemy_database_uri: Optional[PostgresDsn] = None

    @validator("sqlalchemy_database_uri", pre=True)
    def assemble_db_connection(
        cls, value: Optional[str], values: Dict[str, Any]  # noqa: N805,B902
    ) -> Any:
        """Assemble the postgres db connection."""
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("postgres_user"),
            password=values.get("postgres_password"),
            host=str(values.get("postgres_server")),
            port=values.get("postgres_port"),
            path=f"/{values.get('postgres_db') or ''}",
        )

    first_superuser: str
    first_superuser_password: str

    class Config:
        """Extra config."""

        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings."""
    return Settings()


settings = get_settings()
