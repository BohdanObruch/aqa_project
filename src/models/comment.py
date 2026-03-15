from dataclasses import dataclass


@dataclass(frozen=True)
class Comment:
    postId: int
    id: int
    name: str
    email: str
    body: str
