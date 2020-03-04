from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class CategoryPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _product_tile = '//div[@data-product-name="Rambler Colster"]//img[@class="product-tile-image"]'
    _add_to_cart = '//div[@data-product-name="Rambler Colster"]//button[@class="button button-primary add-to-cart"]'
    _customize = '//div[@data-product-name="Rambler Colster"]//span[@class="customizer-button-text"]'
    _swatch = '//div[@data-product-name="Rambler Colster"]//a[@data-yti="black"]'

    def clickProduct(self):
        product_tile = self.driver.find_element(By.XPATH, self._product_tile)
        product_tile.click()

    def clickAddToCartBtn(self):
        time.sleep(5)
        add_to_cart_btn = self.driver.find_element(By.XPATH, self._add_to_cart)
        add_to_cart_btn.click()

    def clickCustomizeBtn(self):
        customize_btn = self.driver.find_element(By.XPATH, self._customize)
        customize_btn.click()

    def clpSwatches(self):
        swatch_color = self.driver.find_element(By.XPATH, self._swatch)
        actions = ActionChains(self.driver)
        actions.move_to_element(swatch_color)
        actions.click(swatch_color).perform()