from runner.test_rest_client import RestClientTest
import pytest


class TestEnvironment:
    def test_setup(self, health_check):
        health_check

    def test_target_environment_TA001(self, target_env):
        a = target_env
        print(a)

    @pytest.mark.skip(reason="Test Case still in implementation phase")
    def test_target_environment_TA002(self, target_env):
        a = target_env
        print(a)
        print(target_env.base_env)
        print(target_env.env_url)
        print("BACKEND URLs--->", target_env.env_backend)
        print(a.env_database)
        print(a.base_user)
        print(a.base_db_user)
        print(a.base_token)

    def test_driver(self, target_env):
        RestClientTest(target_env).run()
