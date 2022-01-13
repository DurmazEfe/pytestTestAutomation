import pytest
from runner.home_page_tests import HomePageTests


@pytest.mark.HomePage
class TestHomePage:

    def test_assert_elements_tab_text(self, web_driver):
        HomePageTests(web_driver).home_page_elements_tab_text_validation()

    def test_assert_forms_tab_text(self, web_driver):
        HomePageTests(web_driver).home_page_forms_tab_text_validation()

    def test_assert_can_navigate_elements_page(self, web_driver):
        HomePageTests(web_driver).elements_tab_navigation()
