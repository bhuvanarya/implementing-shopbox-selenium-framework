from selenium.webdriver.common.by import By


class DeteleAutoListWithProduct:
    def __init__(self, driver):
        self.driver = driver

    wishListMenuPath = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    autolistcountpath = (By.XPATH, "//label[contains(text(),'Automatic')]/following-sibling::span")
    viewAutolist = (By.XPATH, "//label[contains(text(),'Automatic')]/parent::div")
    autoDelete = (By.XPATH, "//mat-icon[contains(text(),'delete')]")
    popupOkButton = (By.XPATH, "//app-popup-confirmation[@class='ng-star-inserted']/div/div[3]/button[2]")
    errormsg = (By.XPATH, "//snack-bar-container[@role='status']/simple-snack-bar/span")
    popupClose = (By.XPATH, "//snack-bar-container[@role='status']/simple-snack-bar/div/button/span")
    viewListPath = (By.XPATH, "//a[starts-with(@href,'/sb/list-cart?listid')]")
    deleteproductspath = (By.XPATH, "//mat-icon[contains(text(),'delete')]")
    backToAutoListPath = (By.XPATH, "//span[contains(text(),'Back to Automatic List')]")

    def clickToViewWishList(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.wishListMenuPath).click()

    def getAutoListCount(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.autolistcountpath).text

    def clickToViewAutoList(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.viewAutolist).click()

    def clickOnDelete(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.autoDelete).click()

    def clickOnPopupOk(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.popupOkButton).click()

    def getErrorMsg(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.errormsg).text

    def closePopMsg(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.popupClose).click()

    def viewAutoListProducts(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.viewListPath).click()

    def getDeleteProductButton(self):
        return self.driver.find_elements(*DeteleAutoListWithProduct.deleteproductspath)

    def getBackToAutoList(self):
        return self.driver.find_element(*DeteleAutoListWithProduct.backToAutoListPath).click()