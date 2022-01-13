import datetime
import pytest
from pathlib import Path
from config import Config
from helpers.browser.chrome import Chrome
from helpers.actions.Login import Login


@pytest.fixture(scope='session')
def target_env(environment):
    # print('\nTests will be run on:', environment)
    cfg = Config(environment)
    return cfg


@pytest.fixture(scope='session')
def target_url(target_env) -> str:
    # print('\nTests will be run on:', target_env)
    url = target_env.env_url
    return url


@pytest.fixture(scope='class')
def health_check(target_env):
    print("Backend ---> ", target_env.env_backend, "UP&RUNNING!!!! <---***")


@pytest.fixture(scope='class')
def web_driver(target_env):
    print("\nSetting up chrome driver")
    driver = Chrome().driver()
    driver.maximize_window()
    Login(driver, target_env).login()
    # driver.get(target_url)
    yield driver
    driver.close()
    print("\nTeardown Driver\n")


@pytest.fixture(scope='session')
def environment(request):
    return request.config.getoption('--env')


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        help='Pass definition of environment'
    )


def pytest_configure(config):
    """
    Set up the output folder, and html report file;
    this has to be done right after the command line options
    are parsed, because we need to rewrite the pytest-html path.
    :param config: pytest Config object to reach terminal options
    :return: None
    """
    option = config.option
    # print(option)
    time_var = datetime.datetime.now()
    report_folder = time_var.strftime('%Y%m%d')
    # create report target dir
    html_report_path = Path('reports/' + report_folder)
    html_report_name = '{}_{}'.format("TestResults", time_var.strftime("%H%M"))
    html_report_path.mkdir(parents=True, exist_ok=True)
    args = f'reports/{report_folder}/{html_report_name}.html'
    option.report = [args]
