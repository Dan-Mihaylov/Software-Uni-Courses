pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
maximum_health = int(input())

stalemate = False
end_game = False

while True:
    command = input().split()

    if command[0] == "Retire":
        stalemate = True
        break
    elif command[0] == "Status":
        repair_sections = list(filter(lambda x: x < maximum_health * 0.20, pirate_ship))
        print(f"{len(repair_sections)} sections need repair.")
        continue

    index = int(command[1])

    if command[0] == "Fire":
        damage = int(command[2])
        if index in range(len(warship)):
            warship[index] = warship[index] - damage
            if warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                break

    elif command[0] == "Defend":
        end_index = int(command[2])
        damage = int(command[3])
        # think 2nd should be bigger than 1st
        if (index in range(len(pirate_ship))) and (end_index in range(len(pirate_ship))):
            for i in range(index, end_index + 1):
                pirate_ship[i] = pirate_ship[i] - damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    end_game = True
                    break

    elif command[0] == "Repair":
        health = int(command[2])
        if index in range(len(pirate_ship)):
            pirate_ship[index] = pirate_ship[index] + health
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health

    if end_game:
        break

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")