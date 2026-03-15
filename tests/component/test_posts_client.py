import pytest
from requests import Response

from src.data.post_payloads import NEW_POST_PAYLOAD
from src.services.posts.client import PostsClient


@pytest.mark.component
def test_posts_client_create_post_builds_expected_request(monkeypatch):
    client = PostsClient(base_url="https://example.test", timeout=3)
    captured_request = {}

    def fake_request(method, url, timeout, **kwargs):
        captured_request["method"] = method
        captured_request["url"] = url
        captured_request["timeout"] = timeout
        captured_request["json"] = kwargs.get("json")

        response = Response()
        response.status_code = 201
        response._content = b'{"id": 101, "userId": 1, "title": "Generated title", "body": "Generated body for API testing"}'
        return response

    monkeypatch.setattr(client.session, "request", fake_request)

    response = client.create_post(NEW_POST_PAYLOAD)

    assert response.status_code == 201
    assert captured_request["method"] == "POST"
    assert captured_request["url"] == "https://example.test/posts"
    assert captured_request["timeout"] == 3
    assert captured_request["json"] == NEW_POST_PAYLOAD
