class CheckoutInformationDTO:
    def __init__(self, 
                 first_name=None,
                 last_name=None,
                 postal_code=None
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code