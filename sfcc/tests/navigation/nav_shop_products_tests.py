# TODO: Need a better assertion to make sure that the page and images render
# TODO: Create an assertion that checks the length of the elements on the page and verifies it equals to the results returned    
# TODO: Action chain method does not work correctly on Firefox
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from sfcc.pages.navigation_page import NavigationPage
import unittest
import time


class NavShopProductsTests(unittest.TestCase):
    
    def tests_product_hard_coolers(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/home'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.maximize_window()

        cooler_nav = NavigationPage(driver)
        cooler_nav.mouseOverCoolers()
        cooler_nav.clickHardCoolers()
        cooler_nav.mouseOverDrinkware()
        cooler_nav.clickTumbler()