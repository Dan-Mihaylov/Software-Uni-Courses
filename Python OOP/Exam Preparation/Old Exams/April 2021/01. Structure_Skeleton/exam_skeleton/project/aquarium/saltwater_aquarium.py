from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    _CAPACITY = 25

    def __init__(self, name: str):
        super(SaltwaterAquarium, self).__init__(name, SaltwaterAquarium._CAPACITY)

    def type(self):
        return self.__class__.__name__
