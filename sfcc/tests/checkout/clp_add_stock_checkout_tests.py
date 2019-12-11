from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.category_page import CategoryPage
import unittest


class ClpAddStockCheckout(unittest.TestCase):

    def tests_add_to_cart(self):
        """Test Scenario:
        1. Navigate to Category Landing Page
        2. Add Stock Glassware to cart
        3. Click on add to cart button
        4. Click on Checkout button
        6. Place order to complete
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.maximize_window()

        clp = CategoryPage(driver)
        clp.clickAddToCartBtn()

