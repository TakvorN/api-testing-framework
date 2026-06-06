import pytest

from api.client import APIClient
from config.settings import JSONPLACEHOLDER_BASE_URL, RESTFUL_BOOKER_BASE_URL


@pytest.fixture
def jsonplaceholder_client():
    return APIClient(JSONPLACEHOLDER_BASE_URL)


@pytest.fixture
def booker_client():
    return APIClient(RESTFUL_BOOKER_BASE_URL)