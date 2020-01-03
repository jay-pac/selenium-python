from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time


class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _pdp_add_to_cart = 'add-to-cart'
    _swatch = '[data-yti={color}]'
    _add_qty = 'input[class="quantity-input custom-quantity-input-pdp valid"]'

    def addToCart(self):
        add_cart_btn = self.driver.find_element(By.ID, self._pdp_add_to_cart)
        action = ActionChains(self.driver)
        action.move_to_element(add_cart_btn)
        action.click(add_cart_btn).perform()

    def clickMiniCart(self):
        time.sleep(5)
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        cart_link.click()

        # Need to remove logic to another class
        checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()
    
    def pdpSwatches(self, color='Black'):
        swatch_color = f'[data-yti={color}]'
        swatches = self.driver.find_element(By.CSS_SELECTOR, swatch_color)
        swatches.click()

    def pdpQuantityField(self, qty=4):
        qty_field = self.driver.find_element(By.CSS_SELECTOR, self._add_qty)
        qty_field.send_keys(qty)
