# I used the get method, to check the values in the meals_info dictionary, so when they pass me another meal, other
# than the pizza, soup and dessert, it was getting added to the dictionary. When in reality it had to stay out.

def shopping_cart(*args):
    max_products = {
        "Pizza": 4,
        "Soup": 3,
        "Dessert": 2
    }

    meals_info = {
        "Pizza": [],
        "Dessert": [],
        "Soup": []
    }

    for arg in args:
        if arg == "Stop":
            break
        meal, product = arg
        if product not in meals_info[meal] and len(meals_info[meal]) < max_products[meal]:
            meals_info[meal].append(product)

    for value in meals_info.values():
        if len(value) > 0:
            break
    else:
        return "No products in the cart!"

    result = ""

    for meal, products in dict(sorted(meals_info.items(), key=lambda x: (-len(x[1]), x[0]))).items():
        result += f"{meal}:\n"
        for product in sorted(products):
            result += f" - {product}\n"

    return result










# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     ('Dessert', 'whatever'),
#     ('Dessert', 'somethinelse'),
#     ('Dessert', 'right'),
#     ('Soup', 'whatever'),
#     ('Soup', 'one more'),
#     'Stop',
# ))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
#
# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test(self):
#         result = shopping_cart(
#             ('Pizza', 'ham'),
#             ('Dessert', 'milk'),
#             ('Pizza', 'ham'),
#             'Stop',
#         )
#         self.assertEqual(result.strip(), "Dessert:\n"
#                                          " - milk\n"
#                                          "Pizza:\n"
#                                          " - ham\n"
#                                          "Soup:")
#
#
# if __name__ == "__main__":
#     unittest.main()