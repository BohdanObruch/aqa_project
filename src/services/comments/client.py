from requests import Response

from src.core.client import BaseApiClient


class CommentsClient(BaseApiClient):
    def get_comment(self, comment_id: int) -> Response:
        return self.request("GET", f"comments/{comment_id}")

    def get_comments_by_post(self, post_id: int) -> Response:
        return self.request("GET", "comments", params={"postId": post_id})
