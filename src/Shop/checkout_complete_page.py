from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.__txt_complete_order = '[data-test="complete-header"]'
        self.__wait = WebDriverWait(self.driver, 10)
    
    def get_txt_complete(self):
        self.__wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.__txt_complete_order)))
        return self.driver.find_element(By.CSS_SELECTOR, self.__txt_complete_order)
    
    def view_checkout_result(self):
        return self.get_txt_complete().text
        