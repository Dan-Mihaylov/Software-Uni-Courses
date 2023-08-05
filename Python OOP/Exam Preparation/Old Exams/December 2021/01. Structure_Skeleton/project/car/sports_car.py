from project.car.car import Car


class SportsCar(Car):

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    def type(self):
        return self.__class__.__name__
