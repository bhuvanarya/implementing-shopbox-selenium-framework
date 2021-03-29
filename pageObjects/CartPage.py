from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    productsGrid = (By.XPATH, "//div[@class='products-inner-div']")
    addToCart = (By.XPATH, "//div[@class='notcartdiv']/span[2]")
    cartIcon = (By.CSS_SELECTOR, "div[class='mat-button-wrapper']")
    cartButton = (By.CSS_SELECTOR, "a[href='/sb/cart']")
    checkOutButton = (By.XPATH, "//span[contains(text(), 'Proceed to Checkout')]")

    def getProductsGrid(self):
        return self.driver.find_elements(*CartPage.productsGrid)

    def clickAddToCart(self):
        return self.driver.find_elements(*CartPage.addToCart)

    def clickCartIcon(self):
        return self.driver.find_element(*CartPage.cartIcon)

    def clickCartButton(self):
        return self.driver.find_element(*CartPage.cartButton)

    def clickCheckOutButton(self):
        return self.driver.find_element(*CartPage.checkOutButton)


