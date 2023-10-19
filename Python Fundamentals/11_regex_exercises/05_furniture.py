import re


text = input()
items_bought = list()
regex = r">>(?P<item>[A-Za-z]+)<<(?P<price>[0-9]+(\.\d+)?)!(?P<quant>[0-9]+)$|(?=\s)"
pattern = re.compile(regex)
total_price = 0
while text != "Purchase":
    matches = re.finditer(pattern, text)
    for match in matches:
        item = match["item"]
        price = float(match["price"])
        quant = int(match["quant"])
        total_price += price * quant
        items_bought.append(item)
    text = input()

print("Bought furniture:")
for item in items_bought:
    print(item)

print(f"Total money spend: {total_price:.2f}")
