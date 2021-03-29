from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    searchKeyword = "Dairy Milk Chocolate 6.6 gms"
    searchField = (By.XPATH, "//input[@placeholder='Search']")
    searchButton = (By.CSS_SELECTOR, "button[class='btn-search']")

    def enterSearchProduct(self):
        return self.driver.find_element(*SearchPage.searchField)

    def clickSearchButton(self):
        return self.driver.find_element(*SearchPage.searchButton)

