import time

from selenium.webdriver.common.by import By


class WalletPage:

    def __init__(self, driver):
        self.driver = driver

    myAccPath = (By.XPATH, "//a[@href='/sb/account/dashboard']")
    walletValuePath = (By.XPATH, "//div[@class='ng-star-inserted']/span")
    viewWallet = (By.XPATH, "//label[starts-with(text(), 'Wallet Amount')]")
    walletDetailsPath = (By.CSS_SELECTOR, "div[class='mat-tab-label-content']")
    promoCashbackpath = (By.XPATH,"//table[starts-with(@class,'table')]/tbody/tr")
    referralTabPath = (By.XPATH,"//*[starts-with(text(), 'Referral Cashback')]")
    noReferralCashback = (By.XPATH, "//*[starts-with(@class, 'mat-body-content')]/div")
    redeemPath = (By.XPATH, "//*[starts-with(text(), 'Redeemed Amount')]")
    redeemCashbackPath = (By.XPATH, "//table[starts-with(@class,'table')]/tbody/tr")

    def viewMyAccount(self):
        return self.driver.find_element(*WalletPage.myAccPath)

    def getWalletAmount(self):
        return self.driver.find_elements(*WalletPage.walletValuePath)

    def viewWalletDetails(self):
        return self.driver.find_element(*WalletPage.viewWallet)

    def getWalletDetails(self):
        return self.driver.find_elements(*WalletPage.walletDetailsPath)

    def getPromoCashbackValues(self):
        return self.driver.find_elements(*WalletPage.promoCashbackpath)

    def viewReferralCashback(self):
        return self.driver.find_element(*WalletPage.referralTabPath)

    def getReferralCashback(self):
        return self.driver.find_element(*WalletPage.noReferralCashback).text

    def viewRedeemCashback(self):
        return self.driver.find_element(*WalletPage.redeemPath)

    def getRedeemCashbackDetails(self):
        return self.driver.find_elements(*WalletPage.redeemCashbackPath)






