from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "Orion"
    app_version: str = "0.1.0"
    environment: str = "development"

    groq_api_key: str
    model_name: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )


# These values are loaded from the environment/.env at runtime. Pylance cannot
# infer environment variables and incorrectly treats them as missing arguments.
settings = Settings()  # pyright: ignore[reportCallIssue]

