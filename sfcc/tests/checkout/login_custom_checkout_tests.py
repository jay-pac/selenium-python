# TODO: Add a Timestamp to the custom text
# TODO: Wait for element to clickable
# TODO: Unable to select the 'customize' button unless scroll into view.
# TODO: Add Assertions to test
from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest


class CustomItemCheckoutTest(unittest.TestCase):

    def tests_custom_check_out(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(base_url)
        driver.maximize_window()

        try:
            splash = driver.find_element(By.XPATH, '//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass
        custom = CustomizePage(driver)
        custom.customModal()

        pdp = ProductPage(driver)
        pdp.addToCart()
        pdp.clickMiniCart()

        checkout = CheckoutPage(driver)
        checkout.signIn('generalOne@user.com', 'Generalone19!')
        checkout.shippingBtn()
        checkout.accountPayment('1111')

        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
