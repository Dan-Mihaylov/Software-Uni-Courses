from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    _TABLE_NUMS = {
        "InsideTable": (1, 50),
        "OutsideTable": (51, 100)
    }

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: [] = []
        self.drink_orders: [] = []
        self.number_of_people: int = 0
        self.is_taken = False

    @property
    def is_reserved(self):
        return self.is_taken == True

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        start, end = Table._TABLE_NUMS[self.type()]
        inside = "Inside table's number must be between 1 and 50 inclusive!"
        outside = "Outside table's number must be between 51 and 100 inclusive!"

        if value not in range(start, end + 1):
            raise ValueError(f"{inside if self.type() == 'InsideTable' else outside}")

        self.__table_number = value

    @abstractmethod
    def type(self):
        ...

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int):
        if not self.is_taken and self.capacity >= number_of_people:
            self.number_of_people = number_of_people
            self.is_taken = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = 0

        for food in self.food_orders:
            total += food.price

        for drink in self.drink_orders:
            total += drink.price

        return total

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_taken = False

    def free_table_info(self):
        if not self.is_taken:
            result = [f"Table: {self.table_number}", f"Type: {self.type()}", f"Capacity: {self.capacity}"]
            return f"\n".join(result)

