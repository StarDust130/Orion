from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Orion"
    app_version: str = "0.1.0"
    environment: str = "development"

    groq_api_key: str
    model_name: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
