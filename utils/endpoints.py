class Endpoints:
    def __init__(self):
        self._endpoint_one = 'search?q=hi'
        self._endpoint_two = 'endpoint/two'

    def endpoint_one(self):
        return self._endpoint_one

    def endpoint_two(self):
        return self._endpoint_two
