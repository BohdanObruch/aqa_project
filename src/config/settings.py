from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True, env_prefix="", extra="ignore")

    base_url: str = Field(default="https://jsonplaceholder.typicode.com", alias="BASE_URL")
    timeout: float = Field(default=10.0, alias="API_TIMEOUT")


settings = Settings()
