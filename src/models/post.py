from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    userId: int
    id: int
    title: str
    body: str
