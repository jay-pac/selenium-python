from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _pdp_add_to_cart = 'add-to-cart'
    _swatch = '[data-yti={color}]'
    _add_qty = 'input[class="quantity-input custom-quantity-input-pdp valid"]'

    def addToCart(self):
        self.driver.execute_script("document.getElementById('add-to-cart').click();")

    def clickMiniCart(self):
        time.sleep(1)
        self.driver.execute_script("document.querySelector('div.mini-cart a.mini-cart-link').click();")

        # TODO Need to remove logic to another Page class
        checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()

    def pdpSwatches(self, color='Black'):
        swatch_color = f'[data-yti={color}]'
        swatches = self.driver.find_element(By.CSS_SELECTOR, swatch_color)
        swatches.click()

    def pdpQuantityField(self, qty=4):
        qty_field = self.driver.find_element(By.CSS_SELECTOR, self._add_qty)
        qty_field.send_keys(qty)
