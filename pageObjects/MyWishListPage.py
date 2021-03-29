import time

from selenium.webdriver.common.by import By


class MyWishListPage:

    def __init__(self, driver):
        self.driver = driver

    wishListMenuPath = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    AutoListCount = (By.XPATH, "//label[starts-with(text(),'Automatic')]/following-sibling::span")
    ManualListCount = (By.XPATH, "//label[starts-with(text(),'Manual')]/following-sibling::span")

    def clickOnWishList(self):
        return self.driver.find_element(*MyWishListPage.wishListMenuPath)

    def getAutoListCount(self):
        return self.driver.find_element(*MyWishListPage.AutoListCount)

    def getManualListCount(self):
        return self.driver.find_element(*MyWishListPage.ManualListCount)




