from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _CAPACITY = 50
    
    def __init__(self, name: str):
        super(FreshwaterAquarium, self).__init__(name, FreshwaterAquarium._CAPACITY)

    def type(self):
        return self.__class__.__name__