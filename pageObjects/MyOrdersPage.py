import time

from selenium.webdriver.common.by import By


class MyOrdersPage:

    def __init__(self, driver):
        self.driver = driver

    myAccPath = (By.XPATH, "//a[@href='/sb/account/dashboard']")
    ordersCountPath = (By.XPATH, "//label[contains(text(), 'rder')]//following-sibling::span")
    viewOrdersPath = (By.XPATH, "//h5[contains(text(), 'Orders')]")
    viewOfflineOrdersPath = (By.XPATH, "//div[starts-with(text(), 'Offline Orders')]")
    offlineOrdersListPath = (By.XPATH, "//tr[@class='ng-star-inserted']")
    viewOnlineOrdersPath = (By.XPATH, "//div[starts-with(text(), 'Online Orders')]")
    noOfRowsPath = (By.XPATH, "//table[starts-with(@class, 'table')]/tbody/tr/td[1]")
    noOfColumnsPath = (By.XPATH, "//table[starts-with(@class, 'table')]/tbody/tr[1]/td")
    viewOnlineOrderPath = (By.XPATH, "//mat-icon[contains(text(), 'remove_red_eye')]")

    OrderNumberPath = (By.XPATH, "//span[starts-with(text(), ' Order - SB_')]")
    orderProductNamePath = (By.XPATH, "//span[@class='pname']")
    orderProductQtyPath = (By.XPATH, "//span[@class='qty']")
    orderTotalPath = (By.XPATH, "//span[contains(text(),'Total')]/following-sibling::span")
    closeOrderPopupPath = (By.XPATH, "//span[starts-with(@class,'close')]/mat-icon")
    homeIcon = (By.XPATH, "//a[@href='/sb/home']")

    def viewMyAccount(self):
        return self.driver.find_element(*MyOrdersPage.myAccPath)

    def getOrdersCount(self):
        return self.driver.find_elements(*MyOrdersPage.ordersCountPath)

    def viewOrders(self):
        return self.driver.find_element(*MyOrdersPage.viewOrdersPath)

    def viewOfflineOrders(self):
        return self.driver.find_element(*MyOrdersPage.viewOfflineOrdersPath)

    def getOfflineOrdersList(self):
        return self.driver.find_elements(*MyOrdersPage.offlineOrdersListPath)

    def viewOnlineOrders(self):
        return self.driver.find_element(*MyOrdersPage.viewOnlineOrdersPath)

    def getNoOfRows(self):
        return self.driver.find_elements(*MyOrdersPage.noOfRowsPath)

    def getNoOfColumns(self):
        return self.driver.find_elements(*MyOrdersPage.noOfColumnsPath)

    def viewOnlineOrder(self):
        return self.driver.find_elements(*MyOrdersPage.viewOnlineOrderPath)

    def getOrderNumber(self):
        return self.driver.find_element(*MyOrdersPage.OrderNumberPath)

    def getOrderProductName(self):
        return self.driver.find_element(*MyOrdersPage.orderProductNamePath)

    def getOrderProductQty(self):
        return self.driver.find_element(*MyOrdersPage.orderProductQtyPath)

    def getOrderTotal(self):
        return self.driver.find_element(*MyOrdersPage.orderTotalPath)

    def closeOrderPopup(self):
        return self.driver.find_element(*MyOrdersPage.closeOrderPopupPath)

    def clickOnHome(self):
        return self.driver.find_element(*MyOrdersPage.homeIcon)






