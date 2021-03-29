import time

from selenium.webdriver.common.by import By


class OrdersPage:

    def __init__(self, driver):
        self.driver = driver

    viewOrderButton = (By.XPATH, "//a[contains(text(),'View Order')]")
    OrderNumber = (By.XPATH, "//div[@class='page-title']/span[1]")
    productName = (By.XPATH, "//span[@class='pname']")

    def clickViewOrder(self):
        return self.driver.find_element(*OrdersPage.viewOrderButton)

    def getOrderNumber(self):
        return self.driver.find_element(*OrdersPage.OrderNumber)

    def getProductName(self):
        return self.driver.find_element(*OrdersPage.productName)

