from page_opjects.page_element import PageElement
from page_opjects.handlers.WebHandlers import WebHandlers
from page_opjects.locators.book_store_application_page_locators import BookStoreApplicationPageLocators


class BookStoreApplicationPage(PageElement):
    def __init__(self, web_driver):
        self._driver = web_driver
        self._by = WebHandlers()
        self._locator = BookStoreApplicationPageLocators()

    def return_home(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.return_home_page)

    def menu_tab_header(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.menu_tab_header)

    def page_header(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.page_header)

    def login_page_menu_navigation(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.login_page)

    def login_username_text_box(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.login_username_text_box)

    def login_password_text_box(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.login_password_text_box)

    def login_button(self):
        return PageElement(self._driver, self._by.xpath(), self._locator.login_button)
