from src.models.user import ApiModel


class Comment(ApiModel):
    postId: int
    id: int
    name: str
    email: str
    body: str
