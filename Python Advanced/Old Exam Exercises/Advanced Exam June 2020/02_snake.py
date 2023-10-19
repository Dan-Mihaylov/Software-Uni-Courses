SIZE = int(input())

burrow_positions = []
snake_pos = []
board = []

for row in range(SIZE):
    board.append(list(input()))
    if "S" in board[row]:
        snake_pos = [row, board[row].index("S")]
        board[snake_pos[0]][snake_pos[1]] = "."

    if "B" in board[row]:
        burrow_positions.append((row, board[row].index("B")))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

food_eaten = 0

while True:
    direction = input()

    next_row, next_col = snake_pos[0] + directions[direction][0], snake_pos[1] + directions[direction][1]

    if 0 <= next_row < SIZE and 0 <= next_col < SIZE:   # If it is a valid position, we continue checks, else break

        if board[next_row][next_col] == "*":
            food_eaten += 1
            board[next_row][next_col] = "."     # put passed through here

        elif board[next_row][next_col] == "B":
            burrow_positions.remove((next_row, next_col))
            board[next_row][next_col] = "."
            exit_position = burrow_positions.pop()
            next_row, next_col = exit_position[0], exit_position[1]
            board[next_row][next_col] = "."

        if food_eaten == 10:
            board[next_row][next_col] = "S"
            print("You won! You fed the snake.")
            break

        else:
            snake_pos = [next_row, next_col]
            board[next_row][next_col] = "."

    else:
        print("Game over!")
        break

print(f"Food eaten: {food_eaten}")
[print(*row, sep="") for row in board]




