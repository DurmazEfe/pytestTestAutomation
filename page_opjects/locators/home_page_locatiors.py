class HomePageLocators:
    img: str = "//div[@id='app']//header//a//img"
    elements: str = "//h5[contains(text(),'Elements')]"
    elements_tab_container: str = "//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']" \
                                  "/div[@class='home-body']/div[@class='category-cards']/div[1]"
    forms: str = "//h5[contains(text(),'Forms')]"
    alerts_frame_windows: str = "//h5[contains(text(),'Alerts, Frame & Windows')]"
    widgets: str = "//h5[contains(text(),'Widgets')]"
    interactions: str = "//h5[contains(text(),'Interactions')]"
    book_store_application: str = "//h5[contains(text(),'Book Store Application')]"
    book_store_application_tab_container: str = '//*[@id="app"]/div/div/div[2]/div/div[6]/div'

