import requests

from config.settings import TIMEOUT


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.timeout = TIMEOUT
        self.session = requests.Session()


    def _build_url(self, endpoint):
        return f"{self.base_url}/{endpoint}"   


    def get(self, endpoint):
        return self.session.get(
            self._build_url(endpoint),
            timeout=self.timeout
        )
    

    def post(self, endpoint, json=None):
        return self.session.post(
            self._build_url(endpoint),
            json=json,
            timeout=self.timeout
        )
    

    def put(self, endpoint, json=None):
        return self.session.put(
            self._build_url(endpoint),
            json=json,
            timeout=self.timeout
        )
    

    def patch(self, endpoint, json=None):
        return self.session.patch(
            self._build_url(endpoint),
            json=json,
            timeout=self.timeout
        )

    def delete(self, endpoint):
        return self.session.delete(
            self._build_url(endpoint),
            timeout=self.timeout
        )