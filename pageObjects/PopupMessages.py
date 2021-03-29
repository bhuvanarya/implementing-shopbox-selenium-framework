from selenium.webdriver.common.by import By


class PopupMessages:

    def __init__(self, driver):
        self.driver = driver

    msgText = (By.XPATH, "//snack-bar-container[@role='status']/simple-snack-bar/span")
    msgButton = (By.XPATH, "//snack-bar-container[@role='status']/simple-snack-bar/div/button/span")

    def getMsg(self):
        return self.driver.find_element(*PopupMessages.msgText)

    def closeMsg(self):
        return self.driver.find_element(*PopupMessages.msgButton)
