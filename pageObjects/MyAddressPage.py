
from selenium.webdriver.common.by import By


class MyAddressPage:

    def __init__(self, driver):
        self.driver = driver

    scrollAccXpath = "//a[@href='/sb/account/dashboard']"
    myAccount = (By.XPATH, "//a[@href='/sb/account/dashboard']")
    # delete
    myAddressPath = (By.XPATH, "//div[@class='title']/h5[contains(text(),'Addresses')]//parent::div")
    myAddressGridPath = (By.XPATH, "//div[@class='contnt']")
    myAddressDeleteButton = (By.XPATH, "//span[@class='delete-add']/mat-icon[1]")
    myAddressDeletePopupButton = (By.XPATH, "//div[@class='dg-footer']/button[2]")
    # Add Address
    addEditAddressTab = (By.XPATH, "//div[contains(text(),'Add/Edit Shipping Address')]")
    addressName = (By.XPATH, "//div[@class='add-ship-address-inner']/div[1]/input")
    pincodeDropdown = (By.XPATH, "//mat-select[@placeholder='Select Pincode']")
    pincodeValuePath = (By.XPATH, "//span[contains(text(),'560043')]")
    pincodeXpath = "//span[contains(text(),'560043')]"
    areaDropDown = (By.XPATH, "//mat-select[@placeholder='Select Area']")
    areaValuePath = (By.XPATH, "//span[contains(text(),' Hennur ')]")
    areaXpath = "//span[contains(text(),' Hennur ')]"
    fullAddressPath = (By.CSS_SELECTOR, "textarea[class*='ng-pristine']")
    landmarkPath = (By.XPATH, "//div[@class='add-ship-address-inner']/div[5]/input")
    mobileNumberPath = (By.XPATH, "//div[@class='add-ship-address-inner']/div[8]/input")
    addressSubmit = (By.XPATH, "//span[contains(text(),'Submit')]")

    # Edit Address
    editScrollXpath = "//div[@class='add-ship-address-inner']/div[8]/input"
    editMyAddressPath = (By.XPATH, "//div[@class='contnt']/div/span[8]/mat-icon")
    updateAddressPath = (By.CSS_SELECTOR, "button[class*='submit-btn']")

    def viewMyAccount(self):
        return self.driver.find_element(*MyAddressPage.myAccount)

    def clickMyAddress(self):
        return self.driver.find_element(*MyAddressPage.myAddressPath)

    def getAddressGrid(self):
        return self.driver.find_element(*MyAddressPage.myAddressGridPath)

    def clickMyAddressDelete(self):
        return self.driver.find_element(*MyAddressPage.myAddressDeleteButton)

    def clickMyAddressDeletePopup(self):
        return self.driver.find_element(*MyAddressPage.myAddressDeletePopupButton)

    def clickAddEditAddressTab(self):
        return self.driver.find_element(*MyAddressPage.addEditAddressTab)

    def enterAddressName(self):
        return self.driver.find_element(*MyAddressPage.addressName)

    def selectPincodeDropdown(self):
        return self.driver.find_element(*MyAddressPage.pincodeDropdown)

    def selectPincodeValue(self):
        return self.driver.find_element(*MyAddressPage.pincodeValuePath)

    def selectAreaDropDown(self):
        return self.driver.find_element(*MyAddressPage.areaDropDown)

    def selectAreaValue(self):
        return self.driver.find_element(*MyAddressPage.areaValuePath)

    def enterFullAddress(self):
        return self.driver.find_element(*MyAddressPage.fullAddressPath)

    def enterLandmark(self):
        return self.driver.find_element(*MyAddressPage.landmarkPath)

    def enterMobileNumber(self):
        return self.driver.find_element(*MyAddressPage.mobileNumberPath)

    def submitAddress(self):
        return self.driver.find_element(*MyAddressPage.addressSubmit)

    def editMyAddress(self):
        return self.driver.find_element(*MyAddressPage.editMyAddressPath)

    def updateAddress(self):
        return self.driver.find_element(*MyAddressPage.updateAddressPath)








