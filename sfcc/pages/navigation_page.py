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
    _hard_cooler = 'nav-item-desktop-hard-coolers'
    _roadie_20 = '//a[contains(text(),"Roadie 20 Hard Cooler")]'
    _cooler_tundra = '//a[contains(text(),”Tundra Hard Coolers”)]'
    _cooler_tank = '//a[contains(text(),”Yeti Tank Ice Buckets”)]'
    _cooler_silo = '//a[contains(text(),”Silo Water Cooler”)]'
    _soft_coolers = 'nav-item-desktop-soft-coolers'
    _cooler_hopper = '//a[contains(text(),”Hopper Soft Coolers”)]'
    _daytrip = '//a[contains(text(),”Daytrip Lunch Bag”)]'
    _custom_hard_coolers = 'nav-item-custom-desktop-hard-coolers'
    _college = '//a[contains(text(),”Collegiate Logos”)]'
    _nascar = '//a[contains(text(),”Nascar Gallery”)]'
    _design = '//a[contains(text(),”Upload Your Own Design”)]'

    _primary_drinkware = '//a[@class="primary-nav-link-yeti"][contains(text(),"Drinkware")]'
    _tumblers = 'nav-item-desktop-drinkware-tumblers'
    _bottles = 'nav-item-desktop-drinkware-bottles'
    _mugs = 'nav-item-desktop-drinkware-mugs'
    _jugs = 'nav-item-desktop-drinkware-jugs'
    _barware = 'nav-item-desktop-drinkware-barware'
    _accessories = 'nav-item-desktop-drinkware-accessories'
    _custom_drinkware = 'nav-item-desktop-drinkware-custom'
    _custom_logo = ''
    _design_gallery = ''

    _primary_bags = '//a[@class="primary-nav-link-yeti"][contains(text(),"Bags")]'
    _waterproof = 'nav-item-desktop-waterproof-bags'
    _bags_camino = '//a[contains(text(),"Camino Carryall Tote")]'
    _panga = '//a[contains(text(),"Panga Dry Bags")]'
    _sidekick = '//a[contains(text(),"Sidekick Dry Gear Case")]'
    _everyday_bags = 'nav-item-desktop-everyday-bags'
    _backpack = '//a[contains(text(),"Crossroads Backpack")]'
    _tote = '//a[contains(text(),"Crossroads Tote")]'
    _bags_daytrip = '2'

    _primary_gear = '//a[@class="primary-nav-link-yeti"][contains(text(),"Gear")]'
    _cargo = 'nav-item-desktop-gear-cargo'
    _bucket = '//a[contains(text(),”Loadout 5 Gallon Bucket”)]'
    _outdoor = 'nav-item-desktop-gear-outdoor'
    _hondo_chair = '//a[contains(text(),’Hondo Chair’)]'
    _blanket = '//a[contains(text(),”Lowlands Blanket”)]'
    _pets = 'nav-item-desktop-gear-pets'
    _dogbowl = '//a[contains(text(), “Dog Bowls”)]'
    _dogbed = '//a[contains(text(),”Trailhead Dog Bed”)]'
    _custom_dogbowls = '//a[contains(text(),”Custom Dog Bowls”)]'
    _apparel = 'nav-item-desktop-gear-apparel'
    _tshirts = '//a[contains(text(),”T-Shirts”)]'
    _hats = '//a[contains(text(),”Hats”)]'
    _gear_accessories = 'nav-item-desktop-gear-accessories'
    _stickers = '//a[contains(text(),”Stickers & Patches”)]'
    _bottle_opener = '//a[contains(text(),”Bottle Openers”)]'

    _primary_accessories = '//a[@class="primary-nav-link-yeti"][contains(text(),"Accessories")]'
    _camino = 'nav-item-desktop-accessories-forcamino'
    _hondo = 'nav-item-desktop-accessories-forhondo'
    _hopper = 'nav-item-desktop-accessories-forhopper'
    _loadout = 'nav-item-desktop-accessories-forloadout'
    _rambler = 'nav-item-desktop-accessories-forrambler'
    _silo = 'nav-item-desktop-accessories-forsilo'
    _tank = 'nav-item-desktop-accessories-fortank'
    _tundra = 'nav-item-desktop-accessories-fortundra'
    _trailhead = 'nav-item-desktop-accessories-fortrailhead'

    _primary_custom = '//a[@class="primary-nav-link-yeti"][contains(text(),"Custom")]'
    _custom_drinkware = 'nav-item-desktop-custom-drinkware'
    _custom_hardcooler = 'nav-item-desktop-custom-hardcoolers'
    _custom_dogbowl = 'nav-item-desktop-custom-dogbowls'
    _custom_corp = 'nav-item-desktop-custom-corporate'

    _primary_this_yeti = '//a[@class="primary-nav-link-yeti"][contains(text(),"This is YETI")]'
    _yeti_story = 'nav-item-desktop-yeti-ourstory'
    _yeti_ambass = 'nav-item-desktop-yeti-ambassadors'
    _yeti_part = 'nav-item-desktop-yeti-partners'
    _yeti_btfw = 'nav-item-destop-yeti-bftw'
    _yeti_stories = 'nav-item-desktop-yeti-stories'
    _yeti_podcasts = 'nav-item-desktop-yeti-podcasts'
    _yeti_news = 'nav-item-desktop-yeti-news'
    _yeti_stores = 'nav-item-desktop-yeti-stores'
    _yeti_domain = '//a[contains(text(),"Austin Domain Northside")]'
    _yeti_austin = '//a[contains(@class,"secondary-nav-link-yeti")][contains(text(),"Austin Flagship")]'
    _yeti_dallas = '//a[contains(@class,"secondary-nav-link-yeti")][contains(text(),"Dallas")]'
    _yeti_chicao = '//a[contains(@class,"secondary-nav-link-yeti")][contains(text(),"Chicago")]'
    _yeti_charleston = '//a[contains(@class,"secondary-nav-link-yeti")][contains(text(),"Charleston")]'

    def mouseOverCoolers(self):
        self.cooler_menu = self.driver.find_element(By.XPATH, self._primary_cooler)

    def mouseOverDrinkware(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_drinkware)

    def mouseOverBags(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_bags)

    def mouseOverGear(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_gear)

    def mouseOverAccess(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_accessories)

    def mouseOverCustom(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_custom)

    def mouseOverYeti(self):
        self.drinkware_menu = self.driver.find_element(By.XPATH, self._primary_this_yeti)

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