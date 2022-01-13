import pytest
from runner.elements_page_tests import ElementsPageTests


@pytest.mark.ElementsPage
class TestElementsPage:

    def test_elements_page_header(self, web_driver):
        ElementsPageTests(web_driver).elements_page_header_verification()
