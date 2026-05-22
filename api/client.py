import requests

from config.settings import BASE_URL, TIMEOUT


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}/{endpoint}",
            timeout=self.timeout
        )
