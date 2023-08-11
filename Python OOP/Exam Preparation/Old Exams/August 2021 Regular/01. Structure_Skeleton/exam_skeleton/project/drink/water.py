from project.drink.drink import Drink


class Water(Drink):
    _PRICE = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super(Water, self).__init__(name, portion, Water._PRICE, brand)

    def type(self):
        return self.__class__.__name__
