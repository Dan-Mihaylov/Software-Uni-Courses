input_list = input().split("|")
initial_budget = float(input())
remaining_budget = initial_budget
markup_prices = []

for items in input_list:
    items_list = items.split("->")
    item = items_list[0]
    price = float(items_list[1])

    if price <= remaining_budget:

        if item == "Clothes" and price <= 50 \
         or item == "Shoes" and price <= 35 \
         or item == "Accessories" and price <= 20.50:
            remaining_budget -= price
            markup_prices.append(price * 1.40)

for i in range(len(markup_prices)):
    print(f"{markup_prices[i]:.2f}", end=" ")

profit = sum(markup_prices) + remaining_budget - initial_budget
print(f"\nProfit: {profit:.2f}")

if sum(markup_prices) + remaining_budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")

