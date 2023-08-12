from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.table.table import Table
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.outside_table import OutsideTable
from project.table.inside_table import InsideTable


class Bakery:

    _FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }

    _DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }

    _TABLE_TYPE = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }


    def __init__(self, name: str):
        self.name = name
        self.food_menu: list= []
        self.drinks_menu: list = []
        self.tables_repository: list = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def _find_food_by_name(self, name:str):
        for food in self.food_menu:
            if food.name == name:
                return food
        return None

    def add_food(self, food_type:str, name: str, price: float):
        found_food = self._find_food_by_name(name)
        if found_food is not None:
            raise Exception(f"{found_food.type()} {name} is already in the menu!")

        if food_type in self._FOOD_TYPES:
            new_food = self._FOOD_TYPES[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

        return

    def _find_drink_by_name(self, name: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink
        return None

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        found_drink = self._find_drink_by_name(name)
        if found_drink is not None:
            raise Exception(f"{found_drink.type()} {name} is already in the menu!")

        if drink_type in self._DRINK_TYPES:
            new_drink = self._DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

        return

    def _find_table_by_number(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table
        return None

    def add_table(self, table_type: str, table_number: int, capacity: int):
        found_table = self._find_table_by_number(table_number)
        if found_table is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self._TABLE_TYPE:
            new_table = self._TABLE_TYPE[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def _find_free_table_for_number_of_people(self, number_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and number_people <= table.capacity:
                return table
        return None

    def reserve_table(self, number_of_people: int):
        found_table = self._find_free_table_for_number_of_people(number_of_people)
        if found_table is None:
            return f"No available table for {number_of_people} people"

        found_table.reserve(number_of_people)
        return f"Table {found_table.table_number} has been reserved for {number_of_people} people"

    def _find_food_by_name(self, food_name: str):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return None

    def order_food(self, table_number: int, *food_names: str):
        found_table = self._find_table_by_number(table_number)
        if found_table is None:
            return f"Could not find table {table_number}"

        found_food_names = []
        missing_food = []

        for name in food_names:
            found_food = self._find_food_by_name(name)
            if found_food is None:
                missing_food.append(name)
            else:
                found_food_names.append(found_food.__repr__())
                found_table.order_food(found_food)

        result = [f"Table {found_table.table_number} ordered:"]
        result.extend(found_food_names)
        result.append(f"{self.name} does not have in the menu:")
        result.extend(missing_food)

        return f"\n".join(result)

    def _find_drink_by_name(self, name: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink
        return None

    def order_drink(self, table_number: int, *drink_names: str):
        found_table = self._find_table_by_number(table_number)
        if found_table is None:
            return f"Could not find table {table_number}"

        found_drink_names = []
        missing_drink_names = []

        for name in drink_names:
            found_drink = self._find_drink_by_name(name)
            if found_drink is None:
                missing_drink_names.append(name)
            else:
                found_drink_names.append(found_drink.__repr__())
                found_table.order_drink(found_drink)

        result = [f"Table {table_number} ordered:"]
        result.extend(found_drink_names)
        result.append(f"{self.name} does not have in the menu:")
        result.extend(missing_drink_names)

        return f"\n".join(result)

    def leave_table(self, table_number: int):
        found_table = self._find_table_by_number(table_number)
        bill_amount = found_table.get_bill()
        self.total_income += bill_amount
        found_table.clear()
        return f"Table: {table_number}\nBill: {bill_amount:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return f"\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


