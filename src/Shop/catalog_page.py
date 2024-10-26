from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.Shop.car_page import CarPage

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.__btn_item_bike_ligth = "add-to-cart-sauce-labs-bike-light"
        self.__btn_item_onesie = "add-to-cart-sauce-labs-onesie"
        self.__car_option = '[data-test="shopping-cart-badge"]'
        self.__wait = WebDriverWait(self.driver, 10)
    
    def get_btn_bike_ligth_add_to_car(self):
        self.__wait.until(EC.element_to_be_clickable((By.NAME, self.__btn_item_bike_ligth)))
        return self.driver.find_element(By.NAME, self.__btn_item_bike_ligth)
    
    def get_btn_onesie_add_to_car(self):
        self.__wait.until(EC.element_to_be_clickable((By.NAME, self.__btn_item_onesie)))
        return self.driver.find_element(By.NAME, self.__btn_item_onesie)
    
    def get_car_option(self):
        self.__wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__car_option)))
        return self.driver.find_element(By.CSS_SELECTOR, self.__car_option)
    
    def add_to_car_bike_ligth_and_onesie(self):
        self.get_btn_bike_ligth_add_to_car().click()
        self.get_btn_onesie_add_to_car().click()
    
    def view_car(self):
        self.get_car_option().click()
        return CarPage(self.driver)

