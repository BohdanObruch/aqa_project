from src.models.comment import Comment
from src.models.post import Post
from src.models.user import Address, Company, Geo, User


def to_post(payload: dict) -> Post:
    return Post(
        userId=payload["userId"],
        id=payload["id"],
        title=payload["title"],
        body=payload["body"],
    )


def to_user(payload: dict) -> User:
    geo = Geo(
        lat=payload["address"]["geo"]["lat"],
        lng=payload["address"]["geo"]["lng"],
    )
    address = Address(
        street=payload["address"]["street"],
        suite=payload["address"]["suite"],
        city=payload["address"]["city"],
        zipcode=payload["address"]["zipcode"],
        geo=geo,
    )
    company = Company(
        name=payload["company"]["name"],
        catchPhrase=payload["company"]["catchPhrase"],
        bs=payload["company"]["bs"],
    )
    return User(
        id=payload["id"],
        name=payload["name"],
        username=payload["username"],
        email=payload["email"],
        address=address,
        phone=payload["phone"],
        website=payload["website"],
        company=company,
    )


def to_comment(payload: dict) -> Comment:
    return Comment(
        postId=payload["postId"],
        id=payload["id"],
        name=payload["name"],
        email=payload["email"],
        body=payload["body"],
    )
