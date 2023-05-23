def grocery_store(**products_info):
    receipts = []

    for product, quant in dict(sorted(products_info.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))).items():
        receipts.append(f"{product}: {quant}")

    return f"\n".join(receipts)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(


    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

