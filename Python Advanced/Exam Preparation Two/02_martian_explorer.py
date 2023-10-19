from collections import deque
SIZE = 6    # SIZE - ROW - MOVEMENT ---> so if it goes out of bound it goes on the other side

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

rover_pos = []
field = []
for row in range(SIZE):
    field.append(input().split())
    if "E" in field[row]:
        rover_pos = [row, field[row].index("E")]

water, metal, concrete = 0, 0, 0
commands = deque(input().split(", "))

while commands:
    move = commands.popleft()

    move_row, move_col = rover_pos[0] + moves[move][0], rover_pos[1] + moves[move][1]

    if move_row == SIZE or move_row < 0:
        move_row = SIZE - abs(move_row)

    if move_col == SIZE or move_col < 0:
        move_col = SIZE - abs(move_col)

    rover_pos = [move_row, move_col]

    if field[move_row][move_col] == "W":
        water += 1
        print(f"Water deposit found at ({move_row}, {move_col})")

    elif field[move_row][move_col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({move_row}, {move_col})")

    elif field[move_row][move_col] == "M":
        metal += 1
        print(f"Metal deposit found at ({move_row}, {move_col})")

    elif field[move_row][move_col] == "R":
        print(f"Rover got broken at ({move_row}, {move_col})")
        break

if all([x > 0 for x in (water, concrete, metal)]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
