import re


line = input()
result_items = []

regex = r"(?P<sep>[#|])(?P<item>[A-Za-z ]+)(?P=sep)" \
        r"(?P<ex>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=sep)" \
        r"(?P<cal>[1-9][0-9]{1,5})(?P=sep)"

pattern = re.compile(regex)
matches = re.finditer(pattern, line)
total_calories = 0

for match in matches:
    total_calories += int(match["cal"])
    result_items.append({"item": match["item"],
                         "ex_date": match["ex"],
                         "calories": match["cal"]})


total_days = int(total_calories / 2000)

print(f"You have food to last you for: {total_days} days!")

for item in result_items:
    print(f"Item: {item['item']}, Best before: {item['ex_date']}, Nutrition: {item['calories']}")
