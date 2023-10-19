size = int(input())

alice_pos = []
total_tea = 0
matrix = []
got_there = True

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]

while True:

    move = input()
    move_row = movement[move][0] + alice_pos[0]
    move_col = movement[move][1] + alice_pos[1]
    matrix[alice_pos[0]][alice_pos[1]] = "*"
    alice_pos = [move_row, move_col]

    if 0 <= move_row < size and 0 <= move_col < size:
        if matrix[move_row][move_col] == "R":
            matrix[move_row][move_col] = "*"
            got_there = False
            break
        elif matrix[move_row][move_col].isnumeric():
            total_tea += int(matrix[move_row][move_col])
    else:
        got_there = False
        break

    if total_tea >= 10:
        matrix[move_row][move_col] = "*"
        break

if got_there:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")
[print(*m) for m in matrix]
