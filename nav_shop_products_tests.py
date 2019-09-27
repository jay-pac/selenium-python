# TODO: Need a better assertion to make sure that the page and images render
# TODO: Create an assertion that checks the length of the elements on the page and verifies it equals to the results returned    
# TODO: Action chain method does not work correctly on Firefox
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import unittest
import time

class NavShopProductsTests(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/home'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)

        try:
            splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass
    
    def tests_product_hard_coolers(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_hardcoolers = self.driver.find_element_by_id('nav-item-hard-coolers')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_hardcoolers)
            actions.click(nav_item_hardcoolers).perform()
        except NoSuchElementException:
            return False
        
        assert "Tundra Ice Chests" in self.driver.title        
    
    def tests_product_soft_coolers(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_softcoolers = self.driver.find_element_by_id('nav-item-soft-coolers')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_softcoolers)
            actions.click(nav_item_softcoolers).perform()
        except NoSuchElementException:
            return False
        
        assert "Hopper Soft Sided Portable Coolers" in self.driver.title   
    
    def tests_product_drinkware(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_drinkware = self.driver.find_element_by_id('nav-item-drinkware')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_drinkware)
            actions.click(nav_item_drinkware).perform()
        except NoSuchElementException:
            return False
        
        assert "Rambler Drinkware Series" in self.driver.title

    def tests_product_bags(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_bags = self.driver.find_element_by_id('nav-item-bags')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_bags)
            actions.click(nav_item_bags).perform()
        except NoSuchElementException:
            return False
        
        assert "Outdoor Gear Bags" in self.driver.title
    
    def tests_product_chargo(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_cargo = self.driver.find_element_by_id('nav-item-cargo')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_cargo)
            actions.click(nav_item_cargo).perform()
        except NoSuchElementException:
            return False
        
        assert "Gear Cases & Buckets" in self.driver.title
    
    def tests_product_chairs(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_chairs = self.driver.find_element_by_id('nav-item-chairs')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_chairs)
            actions.click(nav_item_chairs).perform()
        except NoSuchElementException:
            return False
        
        assert "Hondo Base Camp Camping Chairs" in self.driver.title
    
    def tests_product_accessories(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_acessories = self.driver.find_element_by_id('nav-item-accessories')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_acessories)
            actions.click(nav_item_acessories).perform()
        except NoSuchElementException:
            return False
        
        assert "YETI Accessories & Parts" in self.driver.title
    
    def tests_product_more_gear(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_gear = self.driver.find_element_by_id('nav-item-more-gear')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_gear)
            actions.click(nav_item_gear).perform()
        except NoSuchElementException:
            return False
        
        assert "More Gear | YETI" in self.driver.title
    
    def tests_product_gift_cards(self):
        assert "YETI | Premium Coolers, Drinkware, Gear, and Apparel" in self.driver.title 
        
        shop_menu = self.driver.find_element_by_xpath('//a[@class="nav-level-1-link has-submenu"][contains(text(),"Shop")]')
        nav_item_giftcards = self.driver.find_element_by_id('nav-item-gift-cards')
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(shop_menu)
            actions.move_to_element(nav_item_giftcards)
            actions.click(nav_item_giftcards).perform()
        except NoSuchElementException:
            return False
        
        assert "GIFT CARDS" in self.driver.title
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()