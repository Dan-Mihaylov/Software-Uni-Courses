from abc import ABC, abstractmethod


class Car(ABC):

    __SPEED_LIMITS = {
        "MuscleCar": (250, 450),
        "SportsCar": (400, 600)
    }

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        start, end = Car.__SPEED_LIMITS[self.type()]
        if value not in range(start, end + 1):
            raise ValueError(f"Invalid speed limit! Must be between {start} and {end}!")

        self.__speed_limit = value

    @abstractmethod
    def type(self):
        ...



