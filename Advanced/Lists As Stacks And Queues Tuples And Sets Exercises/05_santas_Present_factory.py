from collections import deque


def craft_present(magic: int, presents_dict: dict):
    for key, value in presents_dict.items():
        if value == magic:
            return key


materials = deque([int(x) for x in input().split()])    # stack
magic_levels = deque([int(x) for x in input().split()])  # queue

available_presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}

pairs = [{"Doll", "Wooden train"}, {"Teddy bear", "Bicycle"}]
presents_crafted = []

# last box of materials, first magic level.

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level
    curr_present = craft_present(product, available_presents)

    if curr_present:
        presents_crafted.append(curr_present)
    else:
        if product < 0:
            materials.append(magic_level + material)
        elif product > 0:
            materials.append(material + 15)

for pair in pairs:
    if pair.issubset(presents_crafted):
        print(f"The presents are crafted! Merry Christmas!")
        break
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")    # reverse because we print the top first
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for toy in sorted(set(presents_crafted)):
    print(f"{toy}: {presents_crafted.count(toy)}")
