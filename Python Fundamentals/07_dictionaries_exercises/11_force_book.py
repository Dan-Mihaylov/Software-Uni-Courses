force_game_info = dict()
# Will store the force sides as keys and users as values in a list.
command = input()


def add_user(user_, side_):
    for users_ in force_game_info.values():
        if user_ in users_:
            return
    force_game_info[side_] = force_game_info.get(side_, []) + [user_]


def change_sides(user_, side_):
    for side, users_ in force_game_info.items():
        if user_ in users_:
            force_game_info[side].remove(user_)
            break
    force_game_info[side_] = force_game_info.get(side_, []) + [user_]


while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        add_user(force_user, force_side)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        change_sides(force_user,force_side)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, users in force_game_info.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
