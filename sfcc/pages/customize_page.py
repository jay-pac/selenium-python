from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time


class CustomizePage():

    def __init__(self, driver):
        self.driver = driver
    
    def customModal(self):
        # need to comment out when using the CLP tests
        time.sleep(5)
        add_custom_btn = self.driver.find_element(By.ID, "add-customization")
        action = ActionChains(self.driver)
        action.move_to_element(add_custom_btn)
        action.click(add_custom_btn).perform()

        try:
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'iframe[data-ycs="customizer"]'))
        except NoSuchElementException:
            return False
            
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="add-text"]').click()
        self.driver.find_element(By.ID, 'design-text').send_keys('AUTOMATION TEST')
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="preview-approve"]').click()
        add_to_cart_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-yti="add-to-cart"]')))
        add_to_cart_btn.click()

        self.driver.switch_to.default_content()