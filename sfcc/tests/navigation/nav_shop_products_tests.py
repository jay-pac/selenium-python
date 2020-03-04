# TODO: Need a better assertion to make sure that the page and images render
# TODO: Create an assertion that checks the length of the elements on the page and verifies it equals to the results returned    
# TODO: Action chain method does not work correctly on Firefox
from sfcc.pages.navigation_page import NavigationPage
import pytest


@pytest.mark.usefixtures("setup")
class TestNavShopProducts():
    
    def tests_product_hard_coolers(self):
        cooler_nav = NavigationPage(self.driver)
        cooler_nav.mouseOverCoolers()
        cooler_nav.clickHardCoolers()
        cooler_nav.mouseOverDrinkware()
        cooler_nav.clickTumbler()