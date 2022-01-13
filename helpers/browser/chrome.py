from helpers.driver.driver import Driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Chrome(Driver):
    def __init__(self):
        self._chrome = webdriver.Chrome(ChromeDriverManager().install())

    def driver(self) -> Driver:
        return Driver(self._chrome)

    @staticmethod
    def name(self) -> str:
        return "Chrome"
