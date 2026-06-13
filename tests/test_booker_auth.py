def test_create_auth_token(auth_token):
    assert isinstance(auth_token, str)
    assert auth_token
