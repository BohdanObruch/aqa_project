import pytest
from pydantic import ValidationError

from src.core.parsers import to_user


@pytest.mark.unit
def test_to_user_maps_nested_payload_to_model():
    payload = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496",
            },
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
    }

    user = to_user(payload)

    assert user.id == 1
    assert user.address.city == "Gwenborough"
    assert user.address.geo.lat == "-37.3159"
    assert user.company.name == "Romaguera-Crona"
    assert user.company.bs == "harness real-time e-markets"


@pytest.mark.unit
def test_to_user_raises_validation_error_for_invalid_payload():
    payload = {
        "id": "wrong-type",
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496",
            },
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
    }

    with pytest.raises(ValidationError):
        to_user(payload)
