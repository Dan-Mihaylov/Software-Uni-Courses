from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_area(self): pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height / 2


class AreaCalculator:

    def __init__(self, shapes):
        if not isinstance(shapes, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total


# shapes = [Rectangle(1, 6), Triangle(2, 3)]
# not_shapes = {Rectangle(1, 7)}
# calculator = AreaCalculator(shapes)
#
# print("The total area is: ", calculator.total_area)
