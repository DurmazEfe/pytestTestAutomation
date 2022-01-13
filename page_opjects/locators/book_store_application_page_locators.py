class BookStoreApplicationPageLocators:
    return_home_page: str = "//div[@id='app']//header//a//img"
    page_header: str = "//div[@class='main-header']"
    menu_tab_header: str = "//div[contains(text(),'Book Store Application')]"
    login_page: str = "//div[contains(@class,'element-list collapse show')]//li[1]"
    login_username_text_box: str = "//input[@id='userName']"
    login_password_text_box: str = "//input[@id='password']"
    login_button: str = "//button[@id='login']"
