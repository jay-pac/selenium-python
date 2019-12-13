from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class CustomDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print(f"Locator type {locatorType} not correct/supported")
        return False

    def getElement(self, locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print(f"Element Found with locator: {locator} locatorType: {locatorType}")
        except:
            print(f"Element not found with locator: {locator} locatorType: {locatorType}")
        return element

    def elementClick(self, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            element.click()
            print(f"Clicked on element with locator: {locator} locatorType: {locatorType}")
        except:
            print(f"Cannot click on the element with locator: {locator} locatorType: {locatorType}")
            print_stack()

    def isElementPresent(self, locatorType, locator):
        try:
            element = self.getElement(locatorType, locator)
            if element is not None:
                print(f"Element Found with locator: {locator} locatorType: {locatorType}")
                return True
            else:
                print(f"Element not found with locator: {locator} locatorType: {locatorType}")
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locatorType, locator, timeout=10,):
        element = None
        try:
            getElement = self.getElement(locatorType, locator)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((getElement,
                                                             "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
