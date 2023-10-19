size = int(input())

battlefield = []
sub_pos = []

for row in range(size):
    battlefield.append(list(input()))
    if "S" in battlefield[row]:
        sub_pos = [row, battlefield[row].index("S")]
        battlefield[sub_pos[0]][sub_pos[1]] = "-"

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

hits = 0
ships_sank = 0

while hits < 3 and ships_sank < 3:

    move = input()

    move_pos = [
        sub_pos[0] + moves[move][0],
        sub_pos[1] + moves[move][1],
    ]

    curr_row, curr_col = move_pos[0], move_pos[1]

    if 0 <= curr_row < size and 0 <= curr_col < size:
        sub_pos = [curr_row, curr_col]

        if battlefield[curr_row][curr_col] == "C":
            battlefield[curr_row][curr_col] = "-"
            ships_sank += 1

        elif battlefield[curr_row][curr_col] == "*":
            battlefield[curr_row][curr_col] = "-"
            hits += 1

battlefield[sub_pos[0]][sub_pos[1]] = "S"

if hits > 2:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_pos[0]}, {sub_pos[1]}]!")
elif ships_sank > 2:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

[print(*row, sep="") for row in battlefield]

