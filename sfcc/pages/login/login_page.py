from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class LoginPage():

    # defining a constructor
    # Provide driver instance
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        email = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login"]//*[@type="email"]')
        email.send_keys(username)

        pwd = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login"]//*[@type="password"]')
        pwd.send_keys(password)

        login_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'dwfrm_login_login')))
        login_btn.click()

