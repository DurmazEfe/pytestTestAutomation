import json
# os.env jsondan okuyup environment'a bassın ordan dağıt
import os


def _read_user():
    print(os.getcwd())
    with open('utils/user.json') as user_file:
        _user = json.load(user_file)
    return _user


def _read_environment():
    with open('utils/environment.json') as environment_file:
        _environment = json.load(environment_file)
    return _environment


class Credentials(object):
    def __init__(self, env):
        self._env = env

    def cred(self):
        x = _read_user()
        y = _read_environment()
        data = {
            "env": y[self._env],
            "user": x[self._env]
        }
        return data


# a = Credentials('dev').cred()
# print(a['env']['url'])
