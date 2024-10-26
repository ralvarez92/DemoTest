from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.Shop.checkout_complete_page import CheckoutCompletePage

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.__btn_finish = "finish"
        self.__wait = WebDriverWait(self.driver, 10)
    
    def get_btn_finish(self):
        self.__wait.until(EC.element_to_be_clickable((By.ID, self.__btn_finish)))
        return self.driver.find_element(By.ID, self.__btn_finish)
    
    def finish_checkout(self):
        self.get_btn_finish().click()
        return CheckoutCompletePage(self.driver)