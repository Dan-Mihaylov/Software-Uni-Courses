from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    _COMFORT = 5
    _PRICE = 10

    def __init__(self):
        super(Plant, self).__init__(Plant._COMFORT, Plant._PRICE)
