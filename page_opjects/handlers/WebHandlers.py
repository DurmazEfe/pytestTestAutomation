from selenium.webdriver.common.by import By


class WebHandlers:
    def __init__(self):
        self._by = By()

    def id(self):
        return self._by.ID

    def xpath(self):
        return self._by.XPATH

    def css_selector(self):
        return self._by.CSS_SELECTOR

    def class_name(self):
        return self._by.CLASS_NAME

    def name(self):
        return self._by.NAME

    def tag_name(self):
        return self._by.TAG_NAME

    def link_text(self):
        return self._by.LINK_TEXT

    def partial_link_text(self):
        return self._by.PARTIAL_LINK_TEXT
