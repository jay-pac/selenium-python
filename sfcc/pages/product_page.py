from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time


class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        add_cart_btn = self.driver.find_element(By.ID, 'add-to-cart')
        action = ActionChains(self.driver)
        action.move_to_element(add_cart_btn)
        action.click(add_cart_btn).perform()

    def clickMiniCart(self):
        time.sleep(5)
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        cart_link.click()

        checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()
