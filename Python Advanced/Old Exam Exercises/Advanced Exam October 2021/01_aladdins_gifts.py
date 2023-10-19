from collections import deque


def check_range(result, counter = 0):
    if counter == 2:
        return False

    if result < 100:
        if result % 2 == 0:
            result = materials[-1] * 2 + magic_levels[0] * 3

        else:
            result = materials[-1] * 2 + magic_levels[0] * 2

        return check_range(result, counter= counter + 1)

    elif result > 499:
        result //= 2

        return check_range(result, counter= counter + 1)

    else:
        return result


materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": range(100, 200),
    "Porcelain Sculpture": range(200, 300),
    "Gold": range(300, 400),
    "Diamond Jewellery": range(400, 500)
}

gifts_needed = (
    {"Gemstone", "Porcelain Sculpture"},
    {"Gold", "Diamond Jewellery"}
)

gifts_created = {}
less_counter = 0

while materials and magic_levels:
    material = materials[-1]
    magic = magic_levels[0]

    result = check_range(material + magic)

    if result:
        for gift in gifts:
            if result in gifts[gift]:
                gifts_created[gift] = gifts_created.get(gift, 0)
                gifts_created[gift] += 1
                break

    materials.pop()
    magic_levels.popleft()


for combination in gifts_needed:
    if len(combination.intersection(gifts_created.keys())) == len(combination):
        print(f"The wedding presents are made!")
        break
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, count in dict(sorted(gifts_created.items(), key=lambda x: x[0])).items():
    print(f"{present}: {count}")


