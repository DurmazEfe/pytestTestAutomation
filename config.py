from utils.credentials import Credentials


class Config:
    def __init__(self, env):
        SUPPORTED_ENV = ['local', 'dev', 'test']

        if env not in SUPPORTED_ENV:
            raise Exception(f'{env} environment is not supported (Use: {SUPPORTED_ENV})')

        cred = Credentials(env).cred()
        # print("Credentials", cred)

        self.base_env = cred['env']

        self.env_url = self.base_env['url']
        self.env_backend = self.base_env['backend']
        self.env_database = self.base_env['database']

        self.base_user = cred['user']
        self.username = self.base_user['username']
        self.password = self.base_user['password']
        self.base_db_user = self.base_user['db']
        self.base_token = self.base_user['token']


# Config('dev')
