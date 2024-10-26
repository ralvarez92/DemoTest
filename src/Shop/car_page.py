from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.Shop.checkout_shopper_information_Page import CheckoutShopperInformationPage

class CarPage:
    def __init__(self, driver):
        self.driver = driver
        self.__btn_checkout = "checkout"
        self.__wait = WebDriverWait(self.driver, 10)
    
    def get_btn_checkout(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__btn_checkout)))
        return self.driver.find_element(By.ID, self.__btn_checkout)

    def do_checkout(self):
        self.get_btn_checkout().click()
        return CheckoutShopperInformationPage(self.driver)