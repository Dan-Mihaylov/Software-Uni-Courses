import re
regex = r"(?<=%)(?P<name>[A-Z][a-z]+)(?=%)|(?<=<)(?P<prod>\w+)(?=>)|" \
        r"|(?<=\|)(?P<quant>[1-9][0-9]*)(?=\|)" \
        r"|(?P<price>[0]\.[0-9]+\$|[1-9][0-9]*(\.{1})?[0-9]*(?=\$))"
match_info = dict()
correct_order = ["name", "prod", "quant", "price"]
total_price = 0


def extract_matches(text: str, pattern: str):
    matches = re.finditer(pattern, text)
    for match in matches:
        if match["name"]:
            match_info["name"] = match_info.get("name", "")
            match_info["name"] = match.group()
        elif match["prod"]:
            match_info["prod"] = match_info.get("prod", "")
            match_info["prod"] = match.group()
        elif match["quant"]:
            match_info["quant"] = match_info.get("quant", "")
            match_info["quant"] = match.group()
        elif match["price"]:
            match_info["price"] = match_info.get("price", "")
            match_info["price"] = match.group()


def check_order(correct: list, item_info: dict):
    for value in correct:
        if value not in item_info:
            return False
    index = 0
    for item in item_info:
        if correct[index] != item:
            return False
        index += 1
    return True


while True:
    line = input()
    if line == "end of shift":
        break

    extract_matches(line, regex)

    if check_order(correct_order, match_info):
        name = match_info["name"]
        product = match_info["prod"]
        price = int(match_info["quant"]) * float(match_info["price"])
        print(f"{name}: {product} - {price:.2f}")
        total_price += price
    match_info.clear()
print(f"Total income: {total_price:.2f}")

