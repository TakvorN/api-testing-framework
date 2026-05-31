import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_existing_post(client, post_id):
    response = client.get(f"posts/{post_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
    assert "userId" in data


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