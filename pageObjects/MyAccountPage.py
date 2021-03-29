import time

from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

    SBIcon = (By.XPATH, "//a[@href='/sb/home']")
    myAccount = (By.XPATH, "//a[@href='/sb/account/dashboard']")
    cancelPopupClose = (By.XPATH, "//span[@class='close c-p']/mat-icon")

    def clickHome(self):
        return self.driver.find_element(*MyAccountPage.SBIcon)

    def viewMyAccount(self):
        return self.driver.find_element(*MyAccountPage.myAccount)












