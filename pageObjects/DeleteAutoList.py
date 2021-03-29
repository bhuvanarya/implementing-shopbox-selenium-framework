import time

from selenium.webdriver.common.by import By


class DeleteAutoList:

    def __init__(self, driver):
        self.driver = driver

    wishListMenuPath = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    viewAutoListPath = (By.XPATH, "//label[starts-with(text(),'Automatic')]/parent::div")
    deleteListIcon = (By.XPATH, "//mat-icon[contains(text(),'delete')]")
    popupOkbutton = (By.XPATH, "//app-popup-confirmation[@class='ng-star-inserted']/div/div[3]/button[2]")
    autolistcountpath = (By.XPATH, "//label[contains(text(),'Automatic')]/following-sibling::span")

    def clickOnWishList(self):
        return self.driver.find_element(*DeleteAutoList.wishListMenuPath)

    def viewAutoListPage(self):
        return self.driver.find_element(*DeleteAutoList.viewAutoListPath)

    def clickOnDeleteListIcon(self):
        return self.driver.find_element(*DeleteAutoList.deleteListIcon)

    def clickOnDeleteListPopup(self):
        return self.driver.find_element(*DeleteAutoList.popupOkbutton)

    def getAutoListCount(self):
        return self.driver.find_element(*DeleteAutoList.autolistcountpath).text






