from requests import Response

from src.core.client import BaseApiClient


class PostsClient(BaseApiClient):
    def get_post(self, post_id: int) -> Response:
        return self.request("GET", f"posts/{post_id}")

    def create_post(self, payload: dict) -> Response:
        return self.request("POST", "posts", json=payload)

    def update_post(self, post_id: int, payload: dict) -> Response:
        return self.request("PUT", f"posts/{post_id}", json=payload)

    def delete_post(self, post_id: int) -> Response:
        return self.request("DELETE", f"posts/{post_id}")
