import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_existing_post(client, post_id):
    response = client.get(f"posts/{post_id}")

    assert response.status_code == 200