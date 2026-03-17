from src.models.user import ApiModel


class Post(ApiModel):
    userId: int
    id: int
    title: str
    body: str
