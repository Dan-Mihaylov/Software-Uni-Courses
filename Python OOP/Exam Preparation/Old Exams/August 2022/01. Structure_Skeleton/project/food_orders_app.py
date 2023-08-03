from project.client import Client


class FoodOrdersApp:
    _receipt_id = 1

    def __init__(self):
        self.menu: list = []                # Menu Objects
        self.clients_list: list = []        # Client Objects

    def _find_client_by_phone_number(self, phone_number: str) -> Client or None:
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client
        return None

    def _check_menu_ready(self) -> bool:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return True

    def _find_meal_by_name(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal
        raise Exception(f"{meal_name} is not on the menu!")

    def register_client(self, client_phone_number: str):
        found_client = self._find_client_by_phone_number(client_phone_number)
        if found_client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        self._check_menu_ready()
        result = [meal.details() for meal in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._check_menu_ready()
        if self._find_client_by_phone_number(client_phone_number) is None:
            self.register_client(client_phone_number)

        client = self._find_client_by_phone_number(client_phone_number)

        current_order = []      # Meal objects, to add to client if everything ok
        current_bill = 0        # Their bill if everything is ok

        for name, quantity in meal_names_and_quantities.items():
            meal = self._find_meal_by_name(name)
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")
            meal.quantity -= quantity
            current_order.append(meal)
            current_bill += meal.price * quantity
            if meal.name not in client.meals_ordered:
                client.meals_ordered[meal.name] = quantity
            else:
                client.meals_ordered[meal.name] += quantity

        client.shopping_cart.extend(current_order)
        client.bill += current_bill

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([meal.name for meal in client.shopping_cart])}" \
               f" for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        client.shopping_cart.clear()
        client.bill = 0

        for meal_name, quantity in client.meals_ordered.items():
            meal = self._find_meal_by_name(meal_name)
            meal.quantity += quantity

        client.meals_ordered = {}

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        result = f"Receipt #{FoodOrdersApp._receipt_id} with total amount of {client.bill:.2f} " \
                 f"was successfully paid for {client_phone_number}."

        client.bill = 0
        client.shopping_cart = []
        FoodOrdersApp._receipt_id += 1

        return result

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} " \
               f"meals on the menu and {len(self.clients_list)} clients."

