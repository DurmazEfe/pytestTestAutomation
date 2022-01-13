import requests


class RestClient:
    def __init__(self, target_env):
        self._be_url = target_env.env_backend
        self._username = target_env.username
        self._password = target_env.password

    def get_app_backend(self, endpoint):
        try:
            response = requests.get(self._be_url + endpoint)
            return response
        except ValueError as error:
            print("--> GET: Problem on getting the response!! <--\n", error)

    def get_app_backend_basic_auth(self, endpoint):
        try:
            response = requests.get(self._be_url + endpoint,
                                    auth=(self._username, self._password))
            return response
        except ValueError as error:
            print("--> GET: Problem on getting the response!! <-- \n", error)

    def post_app_backend_basic_auth(self, endpoint, data):
        try:
            print("rest post---->", self._be_url + endpoint)
            response = requests.get(self._be_url + self._endpoint,
                                    auth=(self._username, self._password),
                                    data=data)
            return response
        except ValueError as error:
            print("--> POST: Problem on getting the response!! <--\n", error)
