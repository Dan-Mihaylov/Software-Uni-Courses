from project.drink.drink import Drink


class Tea(Drink):
    _PRICE = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super(Tea, self).__init__(name, portion, Tea._PRICE, brand)

    def type(self):
        return self.__class__.__name__
