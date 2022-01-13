from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_opjects.handlers.WebHandlers import WebHandlers


class Wait:
    def __init__(self, driver, timeout):
        self._wait: WebDriverWait = WebDriverWait(driver, timeout)

    def for_element_presence_until(self, handler: WebHandlers, locator: str, message: str = ""):
        self._wait.until(ec.presence_of_element_located((handler, locator)), message)

    def for_element_not_presence_until(self, handler: WebHandlers, locator: str, message: str = ""):
        self._wait.until_not(ec.presence_of_element_located((handler, locator)), message)

    def for_element_visibility_until(self, handler: WebHandlers, locator: str, message: str = ""):
        self._wait.until(ec.visibility_of_element_located((handler, locator)), message)

    def for_element_not_visible_until(self, handler: WebHandlers, locator: str, message: str = ""):
        self._wait.until_not(ec.visibility_of_element_located((handler, locator)), message)
