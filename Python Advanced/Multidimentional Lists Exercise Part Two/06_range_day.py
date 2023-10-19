def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * int(steps))    # 1 X 3 == 3, -1 X 3 == -3
    c = my_position[1] + (directions[direction][1] * int(steps))    # 0 x 0 == 0

    if not (0 <= r <= size and 0 <= c < size):  # not going to move if field is out of range
        return my_position
    if field[r][c] == "x":  # not gonna move if field is target
        return my_position
    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:  # we shooting in this direction, until we reach a target
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
field = []

targets = 0
targets_hit = 0

targets_hit_positions = []
my_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(input().split())

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]
        field[row][my_position[1]] = "."

    if "x" in field[row]:
        targets += field[row].count("x")

for _ in range(int(input())):
    line = input().split()

    if line[0] == "move":
        my_position = move(line[1], int(line[2]))   # 1 direction, 2 steps # update my position if move

    elif line[0] == "shoot":
        target_down_pos = shoot(line[1])    # It can return none, if criteria not met

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break
else:
    print(f"Training not completed! {targets - targets_hit} targets left.")

[print(row) for row in targets_hit_positions]

