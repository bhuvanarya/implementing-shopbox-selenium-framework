import time

from selenium.webdriver.common.by import By


class AutomaticListPage:

    def __init__(self, driver):
        self.driver = driver

    wishListMenuIconPath = (By.XPATH, "//a[@href='/sb/account/dashboard?wishlist=1']")
    viewAutoListPath = (By.XPATH, "//label[starts-with(text(),'Automatic')]/parent::div")
    createNewAutoListPath = (By.XPATH, "//div[starts-with(text(), 'Create New')]")
    autodailylistNamePath = (By.XPATH, "//label[starts-with(text(), 'List Name')]/following-sibling::input")
    scheduleTypeDropDown = (By.XPATH, "//label[contains(text(),'Schedule Type')]/following-sibling::mat-select")

    # Daily
    selectScheduleTypeDialyPath = (By.XPATH, "//span[contains(text(),' Daily ')]")
    scheduleHoursDropDown = (By.XPATH, "//label[contains(text(), 'Schedule Hours')]/following-sibling::mat-select")
    selectScheduleHoursPath = (By.XPATH, "//span[contains(text(),'10 am')]")
    createAutoList = (By.XPATH, "//span[contains(text(),'Create')]")

    # Weekly
    autoweeklylistNamePath = (By.XPATH, "//label[starts-with(text(), 'List Name')]/following-sibling::input")
    selectScheduleTypeWeeklyPath = (By.XPATH, "//span[contains(text(),' Weekly ')]")
    scheduleWeekDropDown = (By.XPATH, "//label[contains(text(), 'Schedule Week')]/following-sibling::mat-select")
    selectScheduleWeekPath = (By.XPATH, "//span[contains(text(),'Wednesday')]")

    # Monthly
    automonthlylistNamePath = (By.XPATH, "//label[starts-with(text(), 'List Name')]/following-sibling::input")
    selectScheduleTypemonthlyPath = (By.XPATH, "//span[contains(text(),' Monthly ')]")
    scheduleDateDropdown = (By.XPATH, "//label[contains(text(),'Schedule Date')]/following-sibling::mat-select")
    selectScheduleDatePath = (By.XPATH, "//span[contains(text(), ' 4 ')]")


    def clickOnWishListMenuIcon(self):
        return self.driver.find_element(*AutomaticListPage.wishListMenuIconPath)

    def viewAutoListPage(self):
        return self.driver.find_element(*AutomaticListPage.viewAutoListPath)

    def createNewAutoList(self):
        return self.driver.find_element(*AutomaticListPage.createNewAutoListPath)

    def enterAutoDialylistName(self):
        return self.driver.find_element(*AutomaticListPage.autodailylistNamePath)

    def clickOnScheduleTypeDropDown(self):
        return self.driver.find_element(*AutomaticListPage.scheduleTypeDropDown)

    # Daily
    def selectScheduleTypeDialy(self):
        return self.driver.find_element(*AutomaticListPage.selectScheduleTypeDialyPath)

    def clickOnScheduleHoursDropDown(self):
        return self.driver.find_element(*AutomaticListPage.scheduleHoursDropDown)

    def selectScheduleHours(self):
        return self.driver.find_element(*AutomaticListPage.selectScheduleHoursPath)

    def clickOnCreateAutoList(self):
        return self.driver.find_element(*AutomaticListPage.createAutoList)

    # Weekly
    def enterAutoWeeklylistName(self):
        return self.driver.find_element(*AutomaticListPage.autoweeklylistNamePath)

    def selectScheduleTypeWeekly(self):
        return self.driver.find_element(*AutomaticListPage.selectScheduleTypeWeeklyPath)

    def clickOnScheduleWeekDropDown(self):
        return self.driver.find_element(*AutomaticListPage.scheduleWeekDropDown)

    def selectScheduleWeek(self):
        return self.driver.find_element(*AutomaticListPage.selectScheduleWeekPath)

    # Monthly
    def enterAutoMonthlylistName(self):
        return self.driver.find_element(*AutomaticListPage.automonthlylistNamePath)

    def selectScheduleTypeMonthly(self):
        return self.driver.find_element(*AutomaticListPage.selectScheduleTypemonthlyPath)

    def clickOnScheduleDateDropdown(self):
        return self.driver.find_element(*AutomaticListPage.scheduleDateDropdown)

    def selectScheduleDate(self):
        return self.driver.find_element(*AutomaticListPage.selectScheduleDatePath)




