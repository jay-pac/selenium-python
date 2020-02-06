from selenium.webdriver.common.by import By


class MyWishListPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _add_cart = 'dwfrm_wishlist_items_i0_addToCart'
    _edit_link = 'dwfrm_wishlist_items_i0_updateItem'
    _remove_link = 'dwfrm_wishlist_items_i0_deleteItem'

    def clickAddToCart(self):
        self.driver.execute_script("document.getElementsByName('dwfrm_wishlist_items_i0_addToCart')[0].click();")

    def clickEditLink(self):
        edit_link = self.driver.find_element(By.NAME, self._edit_link)
        edit_link.click()

    def clickRemoveLink(self):
        remove_link = self.driver.find_element(By.NAME, self._remove_link)
        remove_link.click()
