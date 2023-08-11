from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    _PORTION = 200.00

    def __init__(self, name: str, price: float):
        super(Bread, self).__init__(name, Bread._PORTION, price)

    def type(self):
        return self.__class__.__name__
