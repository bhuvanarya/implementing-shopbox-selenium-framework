import time

from selenium.webdriver.common.by import By


class IllustrationPage:

    def __init__(self, driver):
        self.driver = driver

    skipButton = (By.CSS_SELECTOR, "div.skip-div")

    def skip(self):
        return self.driver.find_element(*IllustrationPage.skipButton)

