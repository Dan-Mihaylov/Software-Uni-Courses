from project.dough import Dough
from project.topping import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError(f"The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError(f"You should add dough to the pizza")

        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError(f"The topping's capacity cannot be less or equal to zero")

        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):

        if len(self.toppings) < self.toppings_capacity:
            if topping.topping_type in self.toppings:
                self.toppings[topping.topping_type] += topping.weight
            else:
                self.toppings[topping.topping_type] = topping.weight
            return
        raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return sum(self.toppings.values(), self.dough.weight)

