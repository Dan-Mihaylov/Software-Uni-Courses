from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    _PORTION = 245.00

    def __init__(self, name: str, price: float):
        super(Cake, self).__init__(name, Cake._PORTION, price)

    def type(self):
        return self.__class__.__name__
