from typing import Any, Optional

import requests
from requests import Response
from requests.sessions import Session

from src.config.settings import settings


class BaseApiClient:
    def __init__(self, base_url: Optional[str] = None, timeout: Optional[float] = None) -> None:
        self.base_url = (base_url or settings.base_url).rstrip("/")
        self.timeout = timeout or settings.timeout
        self.session: Session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json; charset=UTF-8"})

    def request(self, method: str, path: str, **kwargs: Any) -> Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.request(method=method, url=url, timeout=self.timeout, **kwargs)
