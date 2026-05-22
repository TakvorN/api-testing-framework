import pytest

from api.client import APIClient


@pytest.fixture
def client():
    return APIClient()