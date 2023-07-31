from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    def food_that_eats(self):
        return [Fruit, Vegetable]

    def gained_weight(self):
        return 0.10

    def make_sound(self):
        return f"Squeak"


class Dog(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40

    def make_sound(self):
        return f"Woof!"


class Cat(Mammal):

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30

    def make_sound(self):
        return f"Meow"

class Tiger(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00

    def make_sound(self):
        return f"ROAR!!!"
