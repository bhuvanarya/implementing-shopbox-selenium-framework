
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    SBIcon = (By.XPATH, "//a[@href='/sb/home']")

    def clickHome(self):
        return self.driver.find_element(*HomePage.SBIcon).click()





