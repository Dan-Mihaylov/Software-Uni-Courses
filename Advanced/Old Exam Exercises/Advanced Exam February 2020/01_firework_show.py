from collections import deque

firework_effect = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

fireworks_made = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while explosive_power and firework_effect:

    if firework_effect[0] <= 0:
        firework_effect.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    curr_effect = firework_effect[0]
    curr_power = explosive_power[-1]
    curr_sum = curr_effect + curr_power

    if curr_sum % 5 == 0 and curr_sum % 3 == 0:
        fireworks_made["Crossette Fireworks"] += 1

    elif curr_sum % 3 == 0:
        fireworks_made["Palm Fireworks"] += 1

    elif curr_sum % 5 == 0:
        fireworks_made["Willow Fireworks"] += 1

    else:
        firework_effect[0] -= 1
        firework_effect.append(firework_effect.popleft())
        continue

    firework_effect.popleft()
    explosive_power.pop()

    if all([x >= 3 for x in fireworks_made.values()]):
        print(f"Congrats! You made the perfect firework show!")
        break
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effect)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for firework, count in fireworks_made.items():
    print(f"{firework}: {count}")

