
from selenium.webdriver.common.by import By


class AddProductList:

    def __init__(self, driver):
        self.driver = driver

    productsGrid = (By.XPATH, "//div[@class='products-inner-div']")
    addToList = (By.XPATH, "//mat-icon[starts-with(@class, 'not-addedlist-icon')]")

    def getProductsGrid(self):
        return self.driver.find_elements(*AddProductList.productsGrid)

    def getAddToListButton(self):
        return self.driver.find_elements(*AddProductList.addToList)





