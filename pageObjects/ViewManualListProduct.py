
from selenium.webdriver.common.by import By


class ViewManualListProduct:

    def __init__(self, driver):
        self.driver = driver

    myWishlistIcon = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    manuallistCountPath = (By.XPATH, "//label[starts-with(text(), 'Manual')]/following-sibling::span")
    manaulListPath = (By.XPATH, "//label[starts-with(text(), 'Manual')]/parent::div")
    baseXpath = "//table[starts-with(@class, 'table')]/tbody"

    def clickOnMyWishList(self):
        return self.driver.find_element(*ViewManualListProduct.myWishlistIcon).click()

    def getManualLIstCount(self):
        return self.driver.find_element(*ViewManualListProduct.manuallistCountPath).text

    def viewManualList(self):
        return self.driver.find_element(*ViewManualListProduct.manaulListPath).click()





