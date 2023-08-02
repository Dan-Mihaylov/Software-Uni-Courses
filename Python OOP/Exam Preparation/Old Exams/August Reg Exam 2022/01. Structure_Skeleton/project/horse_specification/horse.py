from abc import ABC, abstractmethod


class Horse(ABC):

    _TRAINING_GAINS = {
        "Appaloosa": 2,
        "Thoroughbred": 3
    }

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    # TODO One horse can have ONLY ONE rider, one rider can ride only one horse // FIND OUT WHAT IT MEANS //

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed():
            raise ValueError("Horse speed is too high!")

        self.__speed = value

    @abstractmethod
    def max_speed(self):
        ...

    @abstractmethod
    def type(self):
        ...

    def train(self):
        if self.speed + self._TRAINING_GAINS[self.__class__.__name__] > self.max_speed():
            self.speed = self.max_speed()
        else:
            self.speed += self._TRAINING_GAINS[self.__class__.__name__]


