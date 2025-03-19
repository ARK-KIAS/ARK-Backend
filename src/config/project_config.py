from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    EXPIRED_AFTER: int
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
