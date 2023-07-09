class ImageArea:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    # def __lt__(self, other):
    #     return self.get_area() < other.get_area()

    # def __le__(self, other):
    #     return self.get_area() <= other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()


# So you can add only the one result you want to change, example __eq__: self.area == other.area
# it automatically reverses it so you don't have to rewrite the __ne__: self.area != other.area.

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)


