from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self) -> None:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> None:
        pass


class Circle(Shape):

    def __init__(self, radius) -> None:
        super().__init__()
        self.__radius = radius

    def calculate_area(self) -> float:
        return pi * self.__radius * self.__radius

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius


class Rectangle(Shape):

    def __init__(self, width, height) -> None:
        super().__init__()
        self.__height = height
        self.__width = width

    def calculate_area(self) -> float or int:
        return self.__height * self.__width

    def calculate_perimeter(self) -> float or int:
        return 2 * (self.__width + self.__height)