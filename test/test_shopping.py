import pytest
import os
from src.Login.login_page import LoginPage
from src.Factories.checkout_information import CheckoutInformation

@pytest.mark.usefixtures("init_driver")
class TestShopping:

    def test_buy_two_items(self):
        catalog_page = LoginPage(self.driver).login(os.getenv("USERNAME"),
                                                    os.getenv("PASSWORD"))
        catalog_page.add_to_car_bike_ligth_and_onesie()
        checkout = catalog_page.view_car()
        check_steps = checkout.do_checkout()
        information_shopper = CheckoutInformation().information_shopper()
        overview = check_steps.fill_information_shopper(information_shopper)
        shop_complete = overview.finish_checkout()
        assert "Thank you for your order!" == shop_complete.view_checkout_result()

