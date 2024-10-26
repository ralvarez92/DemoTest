from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.__txt_username = "user-name"
        self.__txt_password = "password"
        self.__keys_control = Keys.CONTROL + "a", Keys.DELETE
        self.__wait = WebDriverWait(self.driver, 10)
    
    def get_username(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_username)))
        return self.driver.find_element(By.ID, self.__txt_username)
        #field_username = self.driver.find_element(By.ID, self.__txt_username)
        #field_username.send_keys(self.__keys_control)
        #return field_username
    
    def get_password(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_password)))
        return self.driver.find_element(By.ID, self.__txt_password)
        #field_username = self.driver.find_element(By.ID, self.__txt_password)
        #field_username.send_keys(self.__keys_control)
        #return field_username
    
    def login(self, username, password):
        print(username, password)
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
