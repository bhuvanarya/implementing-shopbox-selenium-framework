from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    checkoutRadio = (By.XPATH, "//div[@class='mat-radio-label-content']")
    cartButton = (By.CSS_SELECTOR, "a[href='/sb/cart']")
    checkOutButton = (By.XPATH, "//span[contains(text(), 'Proceed to Checkout')]")

    # Add new address
    addNewAddressButton = (By.XPATH, "//label[contains(text(),'Add New Address')]")
    addressName = (By.XPATH, "//div[@class='add-ship-address-inner']/div[1]/input")
    pincodeDropdown = (By.XPATH, "//mat-select[@placeholder='Select Pincode']")
    pincodeXpath = "//span[contains(text(),'560043')]"
    selectPincode = (By.XPATH, "//span[contains(text(),'560043')]")
    areaDropdown = (By.XPATH, "//mat-select[@placeholder='Select Area']")
    areaXpath = "//span[contains(text(),' Hennur ')]"
    selectArea = (By.XPATH, "//span[contains(text(),' Hennur ')]")
    address = (By.CSS_SELECTOR, "textarea[class*='ng-pristine']")
    landmark = (By.XPATH, "//div[@class='add-ship-address-inner']/div[5]/input")
    mobileNumber = (By.XPATH, "//div[@class='add-ship-address-inner']/div[8]/input")
    submitAddress = (By.XPATH, "//span[contains(text(),'Submit')]")

    # Time Slots
    datepicker = (By.XPATH, "//mat-datepicker-toggle[@class='mat-datepicker-toggle']/button")
    csspickdate = "mat-calendar[class*='mat-calendar']"
    pickdateCssButton = (By.CSS_SELECTOR, "mat-calendar[class*='mat-calendar']")
    selectDate = (By.XPATH, "//div[contains(text(),'30')]")

    scrollPageXpath = "//div[@class='date']/div/input"
    scrollXpathButton = (By.XPATH, "//div[@class='date']/div/input")
    timeslotpath = (By.XPATH, "//mat-radio-button[@id='mat-radio-15']")

    # Payment Types

    def getcheckoutRadio(self):
        return self.driver.find_elements(*CheckOutPage.checkoutRadio)

    def clickCartButton(self):
        return self.driver.find_element(*CheckOutPage.cartButton)

    def clickCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def clickAddNewAddress(self):
        return self.driver.find_element(*CheckOutPage.addNewAddressButton)

    def enterAddressName(self):
        return self.driver.find_element(*CheckOutPage.addressName)

    def clickPincodeDropdown(self):
        return self.driver.find_element(*CheckOutPage.pincodeDropdown)

    def clickOnPincode(self):
        return self.driver.find_element(*CheckOutPage.selectPincode)

    def clickAreaDropdown(self):
        return self.driver.find_element(*CheckOutPage.areaDropdown)

    def clickOnArea(self):
        return self.driver.find_element(*CheckOutPage.selectArea)

    def enterAddress(self):
        return self.driver.find_element(*CheckOutPage.address)

    def enterLandMark(self):
        return self.driver.find_element(*CheckOutPage.landmark)

    def enterMobileNumber(self):
        return self.driver.find_element(*CheckOutPage.mobileNumber)

    def clickSubmitAddress(self):
        return self.driver.find_element(*CheckOutPage.submitAddress)

    def clickDatePicker(self):
        return self.driver.find_element(*CheckOutPage.datepicker)

    def clickPickDateCssButton(self):
        return self.driver.find_element(*CheckOutPage.pickdateCssButton)

    def clickSelectDate(self):
        return self.driver.find_element(*CheckOutPage.selectDate)

    def clickScrollXpathButton(self):
        return self.driver.find_element(*CheckOutPage.scrollXpathButton)

    def selectTimeSlot(self):
        return self.driver.find_element(*CheckOutPage.timeslotpath)


