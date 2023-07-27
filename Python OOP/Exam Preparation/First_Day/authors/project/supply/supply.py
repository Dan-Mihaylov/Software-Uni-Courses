from abc import ABC, abstractmethod


class Supply(ABC):

    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if value == '':
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self) -> int or float:
        return self.__energy

    @energy.setter
    def energy(self, value) -> None:
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__energy = value

    def details(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
