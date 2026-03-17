from src.models.comment import Comment
from src.models.post import Post
from src.models.user import User


def to_post(payload: dict) -> Post:
    return Post.model_validate(payload)


def to_user(payload: dict) -> User:
    return User.model_validate(payload)


def to_comment(payload: dict) -> Comment:
    return Comment.model_validate(payload)
