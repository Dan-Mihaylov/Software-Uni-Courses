from math import floor


size = int(input())

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

field = []
player_pos = []


for row in range(size):
    field.append([int(x) if x.isnumeric() else x for x in input().split()])
    if "P" in field[row]:
        player_pos = [row, field[row].index("P")]

path = [player_pos]
points = 0

while True:

    direction = input()

    if not direction in moves:
        continue

    new_row, new_col = player_pos[0] + moves[direction][0], player_pos[1] + moves[direction][1]

    if not 0 <= new_row < size:
        if new_row < 0:
            new_row = size - 1
        else:
            new_row = 0

    if not 0 <= new_col < size:
        if new_col < 0:
            new_col = size -1
        else:
            new_col = 0

    if type(field[new_row][new_col]) == int:
        points += field[new_row][new_col]
        field[new_row][new_col] = 0

    elif field[new_row][new_col] == "X":
        points = floor(points / 2)
        print(f"Game over! You've collected {points} coins.\nYour path:")
        path.append([new_row, new_col])
        [print(x) for x in path]
        break

    player_pos = [new_row, new_col]
    path.append([new_row, new_col])

    if points >= 100:
        print(f"You won! You've collected {points} coins.\nYour path:")
        [print(x) for x in path]
        break



