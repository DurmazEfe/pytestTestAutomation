import pytest
from page_opjects.locators.home_page_locatiors import HomePageLocators
from page_opjects.handlers.WebHandlers import WebHandlers
from page_opjects.page_element import PageElement


@pytest.mark.HomePage
class HomePage(PageElement):
    def __init__(self, driver):
        self._by = WebHandlers()
        self._locator = HomePageLocators()
        self._driver = driver

    def page_img(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.img)

    def elements(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.elements)

    def elements_tab_container(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.elements_tab_container)

    def forms(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.forms)

    def alerts_frame_windows(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.alerts_frame_windows)

    def widgets(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.widgets)

    def interactions(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.interactions)

    def book_store_application(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.book_store_application)

    def book_store_application_tab_container(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.book_store_application_tab_container)
