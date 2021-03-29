from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    loginMenuIcon = (By.XPATH, "//mat-icon[contains(text(),'lock')]")
    username = (By.CSS_SELECTOR, "input[type='text']")
    password = (By.CSS_SELECTOR, "input[id='mypass']")
    loginButton = (By.XPATH, "//button[@class='mat-raised-button _mat-animation-noopable']")

    def loginIcon(self):
        return self.driver.find_element(*LoginPage.loginMenuIcon)

    def enterUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def enterPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def lButton(self):
        return self.driver.find_element(*LoginPage.loginButton)
