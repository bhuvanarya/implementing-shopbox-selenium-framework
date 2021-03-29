from selenium.webdriver.common.by import By


class MoveProductsToList:
    def __init__(self, driver):
        self.driver = driver

    viewWishListPath = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    manualListcountPath = (By.XPATH, "//label[starts-with(text(), 'Manual')]/following-sibling::span")
    manualListPath = (By.XPATH, "//label[starts-with(text(),'Manual')]/parent::div")
    viewManualListProduct = (By.XPATH, "//a[starts-with(@href,'/sb/list-cart?listid=')]")
    productCheckBox = (By.XPATH, "//mat-checkbox[starts-with(@class,'sb-checkbox')]")
    moveToPath = (By.XPATH, "//label[contains(text(), 'Select List Type')]/following-sibling::mat-select")
    autolistPath = (By.XPATH, "//span[contains(text(),' Auto ')]")
    dialyListPath = (By.XPATH, "//span[@class='mat-option-text']")
    selectAutoListPath = (By.XPATH, "//label[contains(text(),'Move To')]/following-sibling::mat-select")

    def clickToViewWishList(self):
        return self.driver.find_element(*MoveProductsToList.viewWishListPath).click()

    def getManualListCount(self):
        return self.driver.find_element(*MoveProductsToList.manualListcountPath).text

    def clickToViewManualList(self):
        return self.driver.find_element(*MoveProductsToList.manualListPath).click()

    def clickToViewManualListProducts(self):
        return self.driver.find_element(*MoveProductsToList.viewManualListProduct).click()

    def clickOnCheckBox(self):
        return self.driver.find_elements(*MoveProductsToList.productCheckBox)

    def clickToMoveToList(self):
        return self.driver.find_element(*MoveProductsToList.moveToPath).click()

    def clickToSelectAutoList(self):
        return self.driver.find_element(*MoveProductsToList.autolistPath).click()

    def selectAutoList(self):
        return self.driver.find_element(*MoveProductsToList.selectAutoListPath).click()

    def clickToSelectDailyList(self):
        return self.driver.find_element(*MoveProductsToList.dialyListPath).click()
