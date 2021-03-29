from selenium.webdriver.common.by import By


class AutoListPlaceOrder:
    def __init__(self, driver):
        self.driver = driver

    wishListMenuPath = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    autolistcountpath = (By.XPATH, "//label[contains(text(),'Automatic')]/following-sibling::span")
    viewAutolist = (By.XPATH, "//label[contains(text(),'Automatic')]/parent::div")
    viewAutolistproducts = (By.XPATH, "//a[starts-with(@href,'/sb/list-cart?listid=')]")
    listProccedPath = (By.XPATH, "//button[starts-with(@class,'proceed')]")
    selectPaymentTypesPath = (
    By.XPATH, "//div[starts-with(@class,'payment-type-div')]/mat-radio-group/mat-radio-button[1]")
    placeOrderButton = (By.XPATH, "//span[contains(text(),'Place Order')]")
    viewOrderPath = (By.XPATH, "//a[contains(text(),'View Order')]")
    orderNumberPath = (By.XPATH, "//div[@class='page-title']/span[1]")
    productName = (By.XPATH, "//span[@class='pname']")
    cancelOrderButton = (By.XPATH, "//a[contains(text(),'Cancel')]")
    popupclose = (By.XPATH, "//span[@class='close c-p']/mat-icon")

    def clickToViewWishList(self):
        return self.driver.find_element(*AutoListPlaceOrder.wishListMenuPath).click()

    def getAutoListCount(self):
        return self.driver.find_element(*AutoListPlaceOrder.autolistcountpath).text

    def clickToViewAutoList(self):
        return self.driver.find_element(*AutoListPlaceOrder.viewAutolist).click()

    def clickToViewAutoListProducts(self):
        return self.driver.find_element(*AutoListPlaceOrder.viewAutolistproducts).click()

    def clickToProcced(self):
        return self.driver.find_element(*AutoListPlaceOrder.listProccedPath).click()

    def selectPaymentTypes(self):
        return self.driver.find_element(*AutoListPlaceOrder.selectPaymentTypesPath).click()

    def clickOnPlaceOrder(self):
        return self.driver.find_element(*AutoListPlaceOrder.placeOrderButton).click()

    def clickViewOrder(self):
        return self.driver.find_element(*AutoListPlaceOrder.viewOrderPath).click()

    def getOrderNumber(self):
        return self.driver.find_element(*AutoListPlaceOrder.orderNumberPath).text

    def getproductName(self):
        return self.driver.find_element(*AutoListPlaceOrder.productName).text

    def clickOnCancelOrder(self):
        return self.driver.find_element(*AutoListPlaceOrder.cancelOrderButton).click()

    def clickOnPopupClose(self):
        return self.driver.find_element(*AutoListPlaceOrder.popupclose).click()




