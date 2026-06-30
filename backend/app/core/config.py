from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Business Operations Copilot"
    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    SECRET_KEY: str = "change_this_later"

    FRONTEND_URL: str = "http://localhost:5173"

    DATABASE_URL: str

    GROQ_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()