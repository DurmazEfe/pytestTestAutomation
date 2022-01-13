from page_opjects.locators.elements_page_locators import ElementsPageLocators
from page_opjects.handlers.WebHandlers import WebHandlers
from page_opjects.page_element import PageElement


class ElementsPage(PageElement):
    def __init__(self, driver):
        self._by = WebHandlers()
        self._locator = ElementsPageLocators()
        self._driver = driver

    def page_header(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.page_header)
