import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.PopupMessages import PopupMessages


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fileHandler) # file handler object
        logger.addHandler(ch)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyXpathPresence(self, xpathlocator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpathlocator)))
        wait.until(EC.element_to_be_clickable((By.XPATH, xpathlocator)))

    def verifyCssPresence(self, csslocator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, csslocator)))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, csslocator)))

    def scrollDown(self, scrollXpath):
        scroll_time = 2
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_DOWN)

    def scrollDownArrow(self, scrollXpath):
        scroll_time = 24
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_DOWN)

    def scrollOnceDownArrow(self, scrollXpath):
        scroll_time = 2
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_DOWN)
