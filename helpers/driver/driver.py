class Driver:
    def __init__(self, driver):
        self._driver = driver

    def get(self, url: str):
        self._driver.get(url)

    def set_page_load_timeout(self, time_to_wait):
        self._driver.set_page_load_timeout(time_to_wait)

    def implicitly_wait(self, time_to_wait):
        self._driver.implicity_wait(time_to_wait)

    def find_element(self, by_: str, locator: str):
        return self._driver.find_element(by_, locator)

    def maximize_window(self):
        self._driver.maximize_window()

    def set_window_size(self, width, height):
        self._driver.set_window_size(width, height)

    def execute_script(self, script):
        self._driver.execute_script(script)

    def close(self):
        print("\nTeardown Driver\n")
        self._driver.close()
        self._driver.quit()
