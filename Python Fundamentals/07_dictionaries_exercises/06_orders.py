product_info = dict()

input_info = input().split()

while len(input_info) > 1:
    product = input_info[0]
    price = float(input_info[1])
    quant = int(input_info[2])

    product_info[product] = product_info.get(product, [0, 0])
    temp_info = product_info[product]
    if temp_info[0] != price:
        temp_info[0] = price
    temp_info[1] += quant
    product_info[product] = temp_info

    input_info = input().split()

for product, price_and_quant in product_info.items():
    total_price = price_and_quant[0] * price_and_quant[1]
    print(f"{product} -> {total_price:.2f}")

