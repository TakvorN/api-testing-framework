def test_get_existing_post(client):
    response = client.get("posts/1")

    assert response.status_code == 200