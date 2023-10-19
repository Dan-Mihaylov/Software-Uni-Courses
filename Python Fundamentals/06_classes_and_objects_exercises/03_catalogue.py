class Catalogue:

    def __init__(self, name: str):
        self.name = str(name)
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(str(product_name))

    def get_by_letter(self, first_letter: str):
        asked_products = []
        for product in self.products:
            for letter in product:
                if letter == first_letter:
                    asked_products.append(product)
                break
        return asked_products

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += f"\n".join(sorted(self.products))
        return result



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
