from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    _SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super(SaltwaterFish, self).__init__(name, species, SaltwaterFish._SIZE, price)

    def type(self):
        return self.__class__.__name__

# TODO CAN ONLY LIVE IN SALTWATER AQUARIUM
