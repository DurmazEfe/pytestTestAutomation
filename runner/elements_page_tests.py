from page_opjects.page_elements.home_page import HomePage
from page_opjects.page_elements.elements_page import ElementsPage
import time


class ElementsPageTests:
    def __init__(self, driver):
        self._driver = driver

    def elements_page_navigation(self):
        HomePage(self._driver).elements_tab_container().click()

    def elements_page_header_verification(self):
        self.elements_page_navigation()
        time.sleep(3)
        header = ElementsPage(self._driver).page_header().text()
        assert header == "Elements"
