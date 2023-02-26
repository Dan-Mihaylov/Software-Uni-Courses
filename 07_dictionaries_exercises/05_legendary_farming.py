# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes

legendary_item = None

all_items = {
                "shards": 0,
                "fragments": 0,
                "motes": 0,
                            }

while not legendary_item:
    quantity = []
    item = []
    [quantity.append(int(i)) if i.isnumeric() else item.append(i.lower()) for i in input().split()]

    for i in range(len(quantity)):

        if item[i] in all_items:
            all_items[item[i]] += quantity[i]
        else:
            all_items[item[i]] = quantity[i]
        if all_items["shards"] >= 250:
            all_items["shards"] -= 250
            legendary_item = "Shadowmourne"
            break
        elif all_items["fragments"] >= 250:
            legendary_item = "Valanyr"
            all_items["fragments"] -= 250
            break
        elif all_items["motes"] >= 250:
            legendary_item = "Dragonwrath"
            all_items["motes"] -= 250
            break


print(f"{legendary_item} obtained!")
for key, value in all_items.items():
    print(f"{key}: {value}")

