from helpers.actions.WebDriverWait import Wait


class Actions(Wait):
    def __init__(self, driver):
        self._driver = driver

    def scroll(self, x, y):
        scroll_to = "window.scrollTo({}, {})".format(x, y)
        self._driver.execute_script(scroll_to)
