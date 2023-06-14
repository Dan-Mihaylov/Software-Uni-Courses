def stock_availability(flavours: list, action: str, *args):

    if action == "delivery":

        for arg in args:
            flavours.append(arg)

    elif action == "sell" and args:

        for arg in args:

            if type(arg) == int:
                if len(flavours) <= arg:
                    flavours = []
                else:
                    for _ in range(arg):
                        flavours.pop(0)
            else:
                product = arg
                if product in flavours:

                    while product in flavours:
                        flavours.remove(product)
    else:
        flavours.pop(0)

    return flavours












print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))