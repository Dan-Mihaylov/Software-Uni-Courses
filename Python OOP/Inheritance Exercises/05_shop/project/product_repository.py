from typing import List
from project.product import Product
from project.food import Food
from project.drink import Drink


class ProductRepository:

    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product or None:
        for prod in self.products:
            if prod.name == product_name:
                return prod

    def remove(self, product_name: str) -> None:
        for prod in self.products:
            if prod.name == product_name:
                self.products.remove(prod)

    def __repr__(self) -> str:
        result = []
        for prod in self.products:
            result.append(f"{prod.name}: {prod.quantity}")

        return f"\n".join(result)


# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)

