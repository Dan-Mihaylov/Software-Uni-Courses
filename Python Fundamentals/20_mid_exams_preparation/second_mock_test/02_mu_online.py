all_rooms = input().split("|")

health = 100
bitcoins = 0
is_alive = True
best_room = 0

for room in all_rooms:
    best_room += 1
    room = room.split()
    command = room[0]
    points = int(room[1])

    if command == "potion":
        temp_health = health
        health += points
        if health > 100:
            health = 100
        print(f"You healed for {health - temp_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        monster = command
        health -= points
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            is_alive = False
            break
        else:
            print(f"You slayed {monster}.")

if is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
