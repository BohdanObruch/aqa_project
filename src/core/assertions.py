from typing import Iterable

from requests import Response


def assert_status_code(response: Response, expected_status: int) -> None:
    actual_status = response.status_code
    assert actual_status == expected_status, (
        f"Unexpected status code: expected {expected_status}, got {actual_status}. "
        f"Response body: {response.text}"
    )


def assert_has_keys(payload: dict, expected_keys: Iterable[str]) -> None:
    missing_keys = [key for key in expected_keys if key not in payload]
    assert not missing_keys, f"Response payload is missing keys: {missing_keys}. Payload: {payload}"
