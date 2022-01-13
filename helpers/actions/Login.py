from utils.credentials import Credentials
from helpers.actions.actions import Actions
from page_opjects.page_elements.book_store_application_page import BookStoreApplicationPage
from page_opjects.page_elements.home_page import HomePage
from time import sleep


class Login:
    def __init__(self, driver, target_env):
        self._target_env = target_env
        self._driver = driver

    def login(self):
        url = self._target_env.env_url
        user = self._target_env.base_user
        username = user['username']
        password = user['password']

        print("URL =", url, type(url))
        print("TestUser =", user)
        print("Username =", username)
        print("Password =", password)

        self._driver.get(url)
        book_store_application = BookStoreApplicationPage(self._driver)
        home_page = HomePage(self._driver)

        home_page.book_store_application_tab_container().click()
        sleep(1)
        # book_store_application.menu_tab_header().click()
        Actions(self._driver).scroll(0, 1000)

        book_store_application.login_page_menu_navigation().click()
        sleep(1)

        book_store_application.login_username_text_box().send_keys(username)
        book_store_application.login_password_text_box().send_keys(password)
        sleep(3)
        book_store_application.login_button().click()
        sleep(2)
        book_store_application.return_home().click()
