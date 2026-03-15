from dataclasses import dataclass


@dataclass(frozen=True)
class Geo:
    lat: str
    lng: str


@dataclass(frozen=True)
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


@dataclass(frozen=True)
class Company:
    name: str
    catchPhrase: str
    bs: str


@dataclass(frozen=True)
class User:
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
