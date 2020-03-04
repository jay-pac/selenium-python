from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import os
import time


class CustomizePage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _custom_btn = 'add-customization'
    _add_text = '[data-yti="add-text"]'
    _text = 'design-text'
    _approve = '[data-yti="preview-approve"]'
    _add_to_cart = '[data-yti="add-to-cart"]'
    _swatch = '[data-yti={color}]'
    _back_design = '[data-yti="design-back"]'
    _custom_logo = '[data-yti="upload-logo"]'

    def pdpClickCustomButton(self):
        time.sleep(5)
        add_custom_btn = self.driver.find_element(By.ID, self._custom_btn)
        action = ActionChains(self.driver)
        action.move_to_element(add_custom_btn)
        action.click(add_custom_btn).perform()

    def customModal(self):
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'iframe[data-ycs="customizer"]'))
        except NoSuchElementException:
            return False

        time.sleep(5)

    def selectCustomText(self):
        self.driver.find_element(By.CSS_SELECTOR, self._add_text).click()
        self.driver.find_element(By.ID, self._text).send_keys('AUTOMATION TEST')

    def selectCustomMono(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="monogram"]').click()
        self.driver.find_element(By.ID, 'monogram-text').send_keys('QAT')

    def selectCustomDesign(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="designs"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="yeti-nation"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-name="Built for the Wild - Classic"]').click()

    def selectCustomLogo(self):
        filename = '20.bmp'
        file_path = os.path.join(os.getcwd(), filename)
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="upload-logo"]').click()
        self.driver.find_element(By.NAME, 'upload-image').send_keys(file_path)
        self.driver.find_element(By.CSS_SELECTOR, '[data-ui="confirm-image-rights"]').click()
        time.sleep(3)

    def clickBackDesign(self):
        self.driver.find_element(By.CSS_SELECTOR, self._back_design).click()

    def clickApproval(self):
        self.driver.find_element(By.CSS_SELECTOR, self._approve).click()

    def clickAddToCart(self):
        add_to_cart_btn = WebDriverWait(self.driver, 20, poll_frequency=0.5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._add_to_cart)))
        add_to_cart_btn.click()
        self.driver.switch_to.default_content()

    def addCustomSwatches(self, color='color-black'):
        swatch_color = f'[data-yti={color}]'
        swatches = self.driver.find_element(By.CSS_SELECTOR, swatch_color)
        swatches.click()

    def addNumQtyField(self, num='6'):
        # need to be able clear the field before entering a num.
        # Currently it just adds the value to the end of the field.  So 6 will be 16
        qty_field = self.driver.find_element(By.ID, 'custom-quantity')
        qty_field.clear()
        qty_field.send_keys(num)

    def clickIncrementButton(self):
        increment = self.driver.find_element(By.XPATH, '//button[@class="increment"]')
        x = 1
        while x <= 5:
            increment.click()
            x += 1

    def clickDecrementButton(self):
        decrement = self.driver.find_element(By.XPATH, '//button[@class="decrement"]')
        decrement.click()