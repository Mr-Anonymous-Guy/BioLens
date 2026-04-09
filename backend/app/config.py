from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "BioLens API"
    DEBUG: bool = False
    SECRET_KEY: str = "CHANGE_ME_IN_PRODUCTION_USE_32_CHARS_MIN"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Database
    DATABASE_URL: str = "postgresql://biolens:biolens@postgres:5432/biolens_db"
    ASYNC_DATABASE_URL: str = (
        "postgresql+asyncpg://biolens:biolens@postgres:5432/biolens_db"
    )

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"
    REDIS_CACHE_DB: int = 1

    # RabbitMQ / Celery
    CELERY_BROKER_URL: str = "amqp://biolens:biolens@rabbitmq:5672//"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/2"

    # Qdrant
    QDRANT_HOST: str = "qdrant"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "health_embeddings"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("DEBUG", mode="before")
    @classmethod
    def _parse_debug(cls, value):
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on", "y", "t"}
        return value


settings = Settings()
