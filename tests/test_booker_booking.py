def test_create_booking(created_booking, booking_payload):
    assert isinstance(created_booking["id"], int)

    booking = created_booking["booking"]

    assert booking["firstname"] == booking_payload["firstname"]
    assert booking["lastname"] == booking_payload["lastname"]
    assert booking["totalprice"] == booking_payload["totalprice"]
    assert booking["depositpaid"] == booking_payload["depositpaid"]
    assert booking["bookingdates"] == booking_payload["bookingdates"]
    assert booking["additionalneeds"] == booking_payload["additionalneeds"]


def test_update_booking_with_auth(booker_client, auth_token, created_booking):
    booking_id = created_booking["id"]

    payload = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 250,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-05",
        },
        "additionalneeds": "Dinner",
    }

    headers = {
        "Cookie": f"token={auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = booker_client.put(
        f"booking/{booking_id}",
        json=payload,
        headers=headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["firstname"] == payload["firstname"]
    assert data["lastname"] == payload["lastname"]
    assert data["totalprice"] == payload["totalprice"]
    assert data["depositpaid"] == payload["depositpaid"]
    assert data["bookingdates"] == payload["bookingdates"]
    assert data["additionalneeds"] == payload["additionalneeds"]