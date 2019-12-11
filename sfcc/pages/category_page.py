from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time


class CategoryPage():

    def __init__(self, driver):
        self.driver = driver
    
    def clickProduct(self):
        product_tile = self.driver.find_element(By.XPATH,
                                                '//div[@data-product-name="Rambler Colster"]//img[@class="product-tile-image"]')
        product_tile.click()
    
    def clickAddToCartBtn(self):
        add_to_cart_btn = self.driver.find_element(By.XPATH,
                                                   '//div[@data-product-name="Rambler Colster"]//button[@class="button button-primary add-to-cart"]')
        add_to_cart_btn.click()

    def clickCustomizeBtn(self):
        customize_btn = self.driver.find_element(By.XPATH,
                                                 '//div[@data-product-name="Rambler Colster"]//span[@class="customizer-button-text"]')
        customize_btn.click()
    
    def clpSwatches(self):
        swatch_color = self.driver.find_element(By.XPATH,
                                                '//div[@data-product-name="Rambler Colster"]//a[@data-yti="brick-red"]')
        swatch_color.click()