import time

from selenium.webdriver.common.by import By


class PlaceOrderPage:

    def __init__(self, driver):
        self.driver = driver

    placeOrderPath = (By.XPATH, "//span[contains(text(),'Place Order')]")

    def clickPlaceOrder(self):
        return self.driver.find_element(*PlaceOrderPage.placeOrderPath)



