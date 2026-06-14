import pytest

from api.client import APIClient
from config.settings import JSONPLACEHOLDER_BASE_URL, RESTFUL_BOOKER_BASE_URL


@pytest.fixture
def jsonplaceholder_client():
    return APIClient(JSONPLACEHOLDER_BASE_URL)


@pytest.fixture
def booker_client():
    return APIClient(RESTFUL_BOOKER_BASE_URL)


@pytest.fixture
def auth_token(booker_client):
    payload = {
        "username": "admin",
        "password": "password123",
    }

    response = booker_client.post("auth", json=payload)
    data = response.json()

    return data["token"]


@pytest.fixture
def booking_payload():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-07-01",
            "checkout": "2026-07-10",
        },
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(booker_client, booking_payload):
    response = booker_client.post("booking", json=booking_payload)

    assert response.status_code == 200

    data = response.json()

    return {
        "id": data["bookingid"],
        "booking": data["booking"],
    }