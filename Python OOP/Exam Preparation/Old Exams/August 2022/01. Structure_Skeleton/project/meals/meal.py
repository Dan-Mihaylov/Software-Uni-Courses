from abc import ABC, abstractmethod


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name: str = name
        self.price: float = price       # Price Per Piece
        self.quantity: int = quantity   # How many can you order of those

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Invalid price!")

        self.__price = value

    @abstractmethod
    def details(self):
        ...
