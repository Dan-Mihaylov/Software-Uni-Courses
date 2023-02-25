command = input()
stock = {}

while command != "statistics":
    command = command.split(": ")
    product = command[0]
    quant = int(command[1])

    if product not in stock:
        stock[product] = quant
    else:
        stock[product] += quant

    command = input()

total_quant = 0
for value in stock.values():
    total_quant += value

print(f"Products in stock:")
for product in stock:
    print(f"- {product}: {stock[product]}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {total_quant}")
