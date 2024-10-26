from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.Factories.checkout_information_DTO  import CheckoutInformationDTO
from src.Shop.checkout_overview_page import CheckoutOverviewPage

class CheckoutShopperInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.__txt_first_name = "first-name"
        self.__txt_last_name = "last-name"
        self.__txt_postal_code = "postal-code"
        self.__btn_continue = "continue"
        self.__wait = WebDriverWait(self.driver, 10)
        
    def get_txt_first_name(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_first_name)))
        return self.driver.find_element(By.ID, self.__txt_first_name)
    
    def get_txt_last_name(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_last_name)))
        return self.driver.find_element(By.ID, self.__txt_last_name)
    
    def get_txt_postal_code(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__txt_postal_code)))
        return self.driver.find_element(By.ID, self.__txt_postal_code)
    
    def get_btn_continue(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__btn_continue)))
        return self.driver.find_element(By.ID, self.__btn_continue)
    
    def fill_information_shopper(self, inf = CheckoutInformationDTO()):
        self.get_txt_first_name().send_keys(inf.first_name)
        self.get_txt_last_name().send_keys(inf.last_name)
        self.get_txt_postal_code().send_keys(inf.postal_code)
        self.get_btn_continue().click()
        return CheckoutOverviewPage(self.driver)

