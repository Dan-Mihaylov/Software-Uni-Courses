def shopping_cart(*args):
    max_products = {
        "Pizza": 4,
        "Soup": 3,
        "Dessert": 2
    }
    meals_info = {}

    for arg in args:
        if arg == "Stop":
            break
        meal, product = arg
        meals_info[meal] = meals_info.get(meal, [])
        if product not in meals_info[meal] and len(meals_info[meal]) < max_products[meal]:
            meals_info[meal].append(product)

    if not meals_info:
        return "No products in the cart!"

    result = ""

    for meal, products in dict(sorted(meals_info.items(), key=lambda x: (-len(x[1]), x[0]))).items():
        result += f"{meal}:\n"
        for product in sorted(products):
            result += f" - {product}\n"

    return result










print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
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
