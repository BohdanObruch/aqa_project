import pytest

from src.services.comments.client import CommentsClient
from src.services.posts.client import PostsClient
from src.services.users.client import UsersClient


@pytest.fixture(scope="session")
def posts_client() -> PostsClient:
    return PostsClient()


@pytest.fixture(scope="session")
def users_client() -> UsersClient:
    return UsersClient()


@pytest.fixture(scope="session")
def comments_client() -> CommentsClient:
    return CommentsClient()
