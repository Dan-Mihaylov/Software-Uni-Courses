class PizzaDelivery:

    def __init__(self, name, price: float, ingredients: dict, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):

        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):

        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):

        self.ordered = True
        ingredients = []

        for ing, quant in self.ingredients.items():
            ingredients.append(f"{ing}: {quant}")

        return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients)} and the price will be" \
               f" {self.price}lv."