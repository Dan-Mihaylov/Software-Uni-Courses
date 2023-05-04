
quantity = int(input())         # you should buy each time you go out
days = int(input())

total_spirit = 0
total_spend = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_spend += quantity * 2     # Ornament sets
        total_spirit += 5

    if day % 3 == 0:
        total_spend += (quantity * 5) + (quantity * 3)  # Tree skirts and tree garlands
        total_spirit += 13

    if day % 5 == 0:
        if day % 5 == 0 and day % 3 == 0:
            total_spirit += 30
        total_spend += quantity * 15
        total_spirit += 17

    if day % 10 == 0:
        total_spirit -= 20
        total_spend += 5 + 3 + 15  # Buying one more skirt, garlands, lights because of the cat

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_spend}")
print(f"Total spirit: {total_spirit}")
