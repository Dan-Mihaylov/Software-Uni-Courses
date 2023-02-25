products_and_quant = input().split()
products_needed = input().split()
products = [x for x in products_and_quant if products_and_quant.index(x) % 2 == 0]
quant = [x for x in products_and_quant if products_and_quant.index(x) % 2 != 0]

products_available = {}
for i in range(len(products)):
    products_available[products[i]] = int(quant[i])

for product in products_needed:
    if product in products_available:
        print(f"We have {products_available[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

