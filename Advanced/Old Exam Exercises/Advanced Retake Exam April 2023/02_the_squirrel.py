size = int(input())
moves = input().split(", ")

squirrel_pos = []

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

hazelnuts = 0

for row in range(size):
    field.append(list(input()))
    if "s" in field[row]:
        squirrel_pos = [row, field[row].index("s")]
        field[squirrel_pos[0]][squirrel_pos[1]] = "*"   # find the sq and reset his pos to empty

for move in moves:
    new_row, new_col = squirrel_pos[0] + directions[move][0], squirrel_pos[1] + directions[move][1]

    if 0 <= new_row < size and 0 <= new_col < size:
        squirrel_pos = [new_row, new_col]

        if field[new_row][new_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break

        elif field[new_row][new_col] == "h":
            field[new_row][new_col] = "*"
            hazelnuts += 1
            if hazelnuts == 3:
                print(f"Good job! You have collected all hazelnuts!")
                break
    else:
        print("The squirrel is out of the field.")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")

