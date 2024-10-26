from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from src.Shop.catalog_page import CatalogPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.__txt_username = "user-name"
        self.__txt_password = "password"
        self.__btn_login = "login-button"
        self.__wait = WebDriverWait(self.driver, 10)
    
    def get_username(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_username)))
        return self.driver.find_element(By.ID, self.__txt_username)
    
    def get_password(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_password)))
        return self.driver.find_element(By.ID, self.__txt_password)
    
    def get_loggin_button(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__btn_login)))
        return self.driver.find_element(By.ID, self.__btn_login)
    
    def login(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_loggin_button().click()
        return CatalogPage(self.driver)
