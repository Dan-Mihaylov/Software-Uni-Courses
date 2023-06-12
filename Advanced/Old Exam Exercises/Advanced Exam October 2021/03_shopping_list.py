def shopping_list(budget: int ,**kwargs):

    if budget < 100:
        return f"You do not have enough budget."

    result = ""
    bought_products = []

    for product, info in kwargs.items():
        price_for_products = info[0] * info[1]

        if price_for_products <= budget:
            bought_products.append(product)
            result += f"You bought {product} for {price_for_products:.2f} leva.\n"
            budget -= price_for_products

        if len(bought_products) == 5:
            break

    return result.strip()


















print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


