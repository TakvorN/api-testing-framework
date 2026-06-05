import pytest
from jsonschema import validate

from schemas.post_schema import POST_SCHEMA

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_existing_post(client, post_id):
    response = client.get(f"posts/{post_id}")

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=POST_SCHEMA)

    assert data["id"] == post_id


def test_get_nonexistent_post(client):
    response = client.get("posts/999999")

    assert response.status_code == 404


def test_create_post(client):
    payload = {
        "title": "Test post",
        "body": "This is a test body",
        "userId": 1,
    }

    response = client.post("posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_update_post_with_put(client):
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1,
    }

    response = client.put("posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_update_post_with_patch(client):
    payload = {
        "title": "Partially updated title",
    }

    response = client.patch("posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert "body" in data
    assert "userId" in data


def test_delete_post(client):
    response = client.delete("posts/1")

    assert response.status_code == 200