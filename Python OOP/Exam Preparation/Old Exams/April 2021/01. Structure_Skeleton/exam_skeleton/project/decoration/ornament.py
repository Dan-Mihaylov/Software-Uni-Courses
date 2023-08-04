from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):

    _COMFORT = 1
    _PRICE = 5.00

    def __init__(self):
        super(Ornament, self).__init__(Ornament._COMFORT, Ornament._PRICE)
