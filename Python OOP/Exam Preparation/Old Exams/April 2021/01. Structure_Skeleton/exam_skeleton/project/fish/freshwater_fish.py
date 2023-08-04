from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    _SIZE = 3
    def __init__(self, name: str, species: str, price: float):
        super(FreshwaterFish, self).__init__(name, species, FreshwaterFish._SIZE, price)

    def type(self):
        return self.__class__.__name__
