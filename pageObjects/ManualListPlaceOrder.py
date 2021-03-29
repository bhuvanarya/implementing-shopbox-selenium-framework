from selenium.webdriver.common.by import By


class ManualListPlaceOrder:

    def __init__(self, driver):
        self.driver = driver

    viewManualListDetailsPath = (By.XPATH, "//a[starts-with(@href,'/sb/list-cart?listid')]")
    listProccedPath = (By.XPATH, "//button[starts-with(@class,'proceed')]")
    selectPaymentTypesPath = (By.XPATH, "//div[starts-with(@class,'payment-type-div')]/mat-radio-group/mat-radio-button[1]")
    placeOrderButton = (By.XPATH, "//span[contains(text(),'Place Order')]")
    viewOrderPath = (By.XPATH, "//a[contains(text(),'View Order')]")
    orderNumberPath = (By.XPATH, "//div[@class='page-title']/span[1]")
    productName = (By.XPATH, "//span[@class='pname']")
    cancelOrderButton = (By.XPATH, "//a[contains(text(),'Cancel')]")
    popupclose = (By.XPATH, "//span[@class='close c-p']/mat-icon")

    def viewManualListDetails(self):
        return self.driver.find_element(*ManualListPlaceOrder.viewManualListDetailsPath).click()

    def clickToProcced(self):
        return self.driver.find_element(*ManualListPlaceOrder.listProccedPath).click()

    def selectPaymentTypes(self):
        return self.driver.find_element(*ManualListPlaceOrder.selectPaymentTypesPath).click()

    def clickOnPlaceOrder(self):
        return self.driver.find_element(*ManualListPlaceOrder.placeOrderButton).click()

    def clickViewOrder(self):
        return self.driver.find_element(*ManualListPlaceOrder.viewOrderPath).click()

    def getOrderNumber(self):
        return self.driver.find_element(*ManualListPlaceOrder.orderNumberPath).text

    def getproductName(self):
        return self.driver.find_element(*ManualListPlaceOrder.productName).text

    def clickOnCancelOrder(self):
        return self.driver.find_element(*ManualListPlaceOrder.cancelOrderButton).click()

    def clickOnPopupClose(self):
        return self.driver.find_element(*ManualListPlaceOrder.popupclose).click()





