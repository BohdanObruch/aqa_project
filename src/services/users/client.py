from requests import Response

from src.core.client import BaseApiClient


class UsersClient(BaseApiClient):
    def get_user(self, user_id: int) -> Response:
        return self.request("GET", f"users/{user_id}")
