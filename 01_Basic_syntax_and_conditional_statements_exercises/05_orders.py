
orders_amount = int(input())

total_price = 0

for i in range(orders_amount):
    capsule_price = float(input())
    days = int(input())
    daily_capsules_needed = int(input())

    if 0.01 <= capsule_price <= 100.00 and 1 <= days <= 31 and 1 <= daily_capsules_needed <= 2000:
        coffee_price = daily_capsules_needed * days * capsule_price
        total_price += coffee_price

        print(f'The price for the coffee is: ${coffee_price:.2f}')

print(f"Total: ${total_price:.2f}")
