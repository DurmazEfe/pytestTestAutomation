from helpers.actions.WebDriverWait import Wait
from page_opjects.handlers.WebHandlers import WebHandlers
from page_opjects import locators
from helpers.driver import driver


class PageElement:
    def __init__(self, web_driver, handler, locator):
        self._handler: WebHandlers = handler
        self._locator: locators = locator
        self._driver: driver = web_driver

    def set_handler(self, custom_handler: WebHandlers) -> WebHandlers:
        self._locator = custom_handler

    def set_locator(self, custom_locator: locators):
        self._locator = custom_locator

    def element(self):
        return self._driver.find_element(self._handler, self._locator)

    def found_handler(self) -> WebHandlers:
        return self._handler

    def found_locator(self) -> locators:
        return self._locator

    def text(self) -> str:
        return self._driver.find_element(self._handler, self._locator).text

    def is_displayed(self) -> bool:
        return self._driver.find_element(self._handler, self._locator).is_displayed()

    def click(self):
        Wait(self._driver, 10).for_element_presence_until(self._handler, self._locator)
        self._driver.find_element(self._handler, self._locator).click()

    def send_keys(self, value):
        Wait(self._driver, 10).for_element_presence_until(self._handler, self._locator)
        self._driver.find_element(self._handler, self._locator).send_keys(value)

    def clear(self):
        Wait(self._driver, 10).for_element_presence_until(self._handler, self._locator)
        self._driver.find_element(self._handler, self._locator).clear()

