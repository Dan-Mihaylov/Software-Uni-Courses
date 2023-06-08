from collections import deque

# FML

elfs_energy = deque([int(x) for x in input().split()])          # We take first elf
materials_in_box = deque([int(x) for x in input().split()])     # We take last box

counter = 0     # To count if it is every 3rd or 5th time
total_toys = 0
total_energy = 0

while elfs_energy and materials_in_box:

    initial_elf_energy = elfs_energy.popleft()
    current_elf_energy = initial_elf_energy
    current_box = materials_in_box.pop()    # last
    energy_spent = 0
    toys_created = 0
    reward = 0
    counter += 1

    if current_elf_energy < 5:
        materials_in_box.append(current_box)
        continue

    if current_elf_energy >= current_box:
        toys_created += 1
        current_elf_energy -= current_box
        energy_spent = current_box
        reward += 1

        if counter % 3 == 0:

            if current_elf_energy >= current_box:
                current_elf_energy -= current_box
                energy_spent += current_box
                toys_created += 1

            else:
                elfs_energy.append(initial_elf_energy * 2)
                materials_in_box.append(current_box)
                continue

        if counter % 5 == 0:
            toys_created = 0
            reward = 0


    else:
        elfs_energy.append(initial_elf_energy * 2)
        materials_in_box.append(current_box)
        continue

    total_energy += energy_spent
    total_toys += toys_created
    elfs_energy.append(current_elf_energy + reward)


print(total_energy, total_toys)
if elfs_energy:
    print(elfs_energy)
if materials_in_box:
    print(materials_in_box)