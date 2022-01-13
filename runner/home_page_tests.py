from page_opjects.page_elements.home_page import HomePage
from page_opjects.page_elements.elements_page import ElementsPage
import time


class HomePageTests:
    def __init__(self, driver):
        self._driver = driver
        self._home_page = HomePage(self._driver)
        self._elements_page = ElementsPage(self._driver)

    def home_page_elements_tab_text_validation(self):
        text = self._home_page.elements().text()
        print("\nUI Value:", text)
        assert text == "Elements"

    def home_page_forms_tab_text_validation(self):
        text = self._home_page.forms().text()
        print("\nUI Value:", text)
        assert text == "Forms"

    def elements_tab_navigation(self):
        self._home_page.elements_tab_container().click()
        time.sleep(3)
        header = self._elements_page.page_header().text()
        print("\nUI Value:", header)
        assert header == "Elements"
