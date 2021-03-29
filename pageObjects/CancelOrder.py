import time

from selenium.webdriver.common.by import By


class CancelOrder:

    def __init__(self, driver):
        self.driver = driver

    cancelOrderButton = (By.XPATH, "//a[contains(text(),'Cancel')]")
    cancelPopupClose = (By.XPATH, "//span[@class='close c-p']/mat-icon")

    def clickCancelOrder(self):
        return self.driver.find_element(*CancelOrder.cancelOrderButton)

    def closeCancelPopup(self):
        return self.driver.find_element(*CancelOrder.cancelPopupClose)




