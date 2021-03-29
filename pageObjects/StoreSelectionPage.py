import time

from selenium.webdriver.common.by import By


class StoreSelectionPage:

    def __init__(self, driver):
        self.driver = driver

    stores = (By.CSS_SELECTOR, "div.section>div")
    shopnow = (By.CSS_SELECTOR, "[class*='mat-raised-button']")

    def activeStores(self):
        return self.driver.find_elements(*StoreSelectionPage.stores)

    def storeShopNow(self):
        return self.driver.find_element(*StoreSelectionPage.shopnow)
