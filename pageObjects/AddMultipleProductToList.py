from selenium.webdriver.common.by import By


class AddMultipleProductToList:
    def __init__(self, driver):
        self.driver = driver

    searchproduct = "Dairy Milk C"
    searchInputPath = (By.XPATH, "//input[@placeholder='Search']")
    clickToSearch = (By.XPATH, "//button[@class='btn-search']")
    productsGridPath = (By.XPATH, "//div[@class='p-name']")
    addToListPath = (By.XPATH, "//mat-icon[starts-with(@class, 'not-addedlist-icon')]")
    searchproductgrid = (By.XPATH, "//div[starts-with(@class,'all-products')]/div[2]/div")

    def enterSearchkeyword(self):
        return self.driver.find_element(*AddMultipleProductToList.searchInputPath).send_keys(*AddMultipleProductToList.searchproduct)

    def clickToSearchProduct(self):
        return self.driver.find_element(*AddMultipleProductToList.clickToSearch).click()

    def getProductGrids(self):
        return self.driver.find_elements(*AddMultipleProductToList.productsGridPath)

    def getAddToListButtons(self):
        return self.driver.find_elements(*AddMultipleProductToList.addToListPath)

    def getSearchProductGridLength(self):
        return self.driver.find_elements(*AddMultipleProductToList.searchproductgrid)




