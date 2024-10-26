import pytest
import os
from src.Login.loginPage import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_buy_two_items(self):
        #Login
        print(os.getenv("USERNAME"))
        #main_page = LoginPage(self.driver).login(os.getenv("USERNAME"),
        #                                         os.getenv("PASSWORD"))