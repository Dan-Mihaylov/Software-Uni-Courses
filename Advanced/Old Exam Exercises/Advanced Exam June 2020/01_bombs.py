from collections import deque

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casing = deque([int(x) for x in input().split(", ")])

materials_needed = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

bombs_created = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effect and bomb_casing:
    curr_effect = bomb_effect.popleft()
    curr_casing = bomb_casing.pop()

    while True:
        result = curr_effect + curr_casing
        if result in materials_needed.keys():
            bombs_created[materials_needed[result]] += 1
            break
        else:
            curr_casing -= 5

    if all([x >= 3 for x in bombs_created.values()]):
        print(f"Bene! You have successfully filled the bomb pouch!")
        break

else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")

if not bomb_casing:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")

for bomb, count in bombs_created.items():
    print(f"{bomb}: {count}")






