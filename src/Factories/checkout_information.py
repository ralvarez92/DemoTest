from faker import Faker
from src.Factories.checkout_information_DTO import CheckoutInformationDTO

class CheckoutInformation:
    def __init__(self):
        self.fake = Faker()
    
    def information_shopper(self):
        return CheckoutInformationDTO(first_name= self.fake.first_name(),
                                      last_name= self.fake.first_name(),
                                      postal_code= self.fake.zipcode())