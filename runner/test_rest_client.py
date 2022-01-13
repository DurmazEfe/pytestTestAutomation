from helpers.RestClient import RestClient
from utils.endpoints import Endpoints


class RestClientTest:
    def __init__(self, env):
        self._env = env
        self._endpoints = Endpoints()

    def run(self):
        response = RestClient(self._env).get_app_backend(self._endpoints.endpoint_one())
        print(response.status_code, type(response))
        assert str(response.status_code) == '200'
