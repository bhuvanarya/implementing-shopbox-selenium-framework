
from selenium.webdriver.common.by import By


class DeleteManualList:

    def __init__(self, driver):
        self.driver = driver

    manualDelete = (By.XPATH, "//mat-icon[contains(text(),'delete')]")
    popupOkButton = (By.XPATH, "//app-popup-confirmation[@class='ng-star-inserted']/div/div[3]/button[2]")
    errormsg = (By.XPATH, "//snack-bar-container[@role='status']/simple-snack-bar/span")
    popupClose = (By.XPATH, "//snack-bar-container[@role='status']/simple-snack-bar/div/button/span")
    viewListPath = (By.XPATH, "//a[starts-with(@href,'/sb/list-cart?listid')]")
    pnamePath = (By.XPATH, "//span[@class='pname']")
    deleteProduct = (By.XPATH, "//td[@class='mc-remove']")
    backToManual = (By.XPATH, "//span[contains(text(),'Back to Manual List')]")

    def clickOnDeleteSingleManuallist(self):
        return self.driver.find_element(*DeleteManualList.manualDelete).click()

    def clickOnPopupOk(self):
        return self.driver.find_element(*DeleteManualList.popupOkButton).click()

    def getErrorMsg(self):
        return self.driver.find_element(*DeleteManualList.errormsg).text

    def closePopMsg(self):
        return self.driver.find_element(*DeleteManualList.popupClose).click()

    def viewManualList(self):
        return self.driver.find_element(*DeleteManualList.viewListPath).click()

    def getProductName(self):
        return self.driver.find_element(*DeleteManualList.pnamePath).text

    def deleteProductFromList(self):
        return self.driver.find_element(*DeleteManualList.deleteProduct).click()

    def backToManualList(self):
        return self.driver.find_element(*DeleteManualList.backToManual).click()







