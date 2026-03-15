from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    timeout: float = float(os.getenv("API_TIMEOUT", "10"))


settings = Settings()
