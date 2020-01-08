from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *

class NavigationPage():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _primary_cooler = '//a[@class="primary-nav-link-yeti"][contains(text(),"Coolers")]'
    _primary_drinkware = '//a[@class="primary-nav-link-yeti"][contains(text(),"Drinkware")]'
    _primary_bags = '//a[@class="primary-nav-link-yeti"][contains(text(),"Bags")]'
    _primary_gear = '//a[@class="primary-nav-link-yeti"][contains(text(),"Gear")]'
    _primary_accessories = '//a[@class="primary-nav-link-yeti"][contains(text(),"Accessories")]'
    _primary_custom = '//a[@class="primary-nav-link-yeti"][contains(text(),"Custom")]'
    _primary_this_yeti = '//a[@class="primary-nav-link-yeti"][contains(text(),"This is YETI")]'
    _hard_cooler = 'nav-item-desktop-hard-coolers'
    _tumblers = 'nav-item-desktop-drinkware-tumblers'
    _waterproof = 'nav-item-desktop-waterproof-bags'
    _cargo = 'nav-item-desktop-gear-cargo'

    def mouseOverCoolers(self):
        self.cooler_menu = self.driver.find_element(By.XPATH, self._primary_cooler )
    
    def mouseOverDrinkware(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_drinkware )

    def clickHardCoolers(self):
        nav_item_hardcoolers = self.driver.find_element(By.ID, self._hard_cooler)
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(self.cooler_menu)
            actions.move_to_element(nav_item_hardcoolers)
            actions.click(nav_item_hardcoolers).perform()
        except NoSuchElementException:
            return False
        
        assert "Tundra Ice Chests" in self.driver.title  
    
    def clickTumbler(self):
        nav_item_tumblers = self.driver.find_element(By.ID, self._tumblers)
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(self.drinkware_menu)
            actions.move_to_element(nav_item_tumblers)
            actions.click(nav_item_tumblers).perform()
        except NoSuchElementException:
            return False
        
        assert "Tumblers" in self.driver.title  
    
    def clickBags(self):
        pass
    
    def clickGear(self):
        pass
    
    def clickAccessories(self):
        pass
    
    def clickCustom(self):
        pass
    
    def clickThisYeti(self):
        pass
    