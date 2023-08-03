class Client:

    def __init__(self, phone_number: str):
        self.phone_number: str = phone_number
        self.shopping_cart: list = []   # [meal: Objects]
        self.bill = 0.0
        self.meals_ordered = {}     # {Meal Name: Quantity}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if value.startswith("0") and all([x.isnumeric() for x in value]) and len(value) == 10:
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")

    # TODO / Add a method to set bill to whatever the client has to pay, from shopping cart




