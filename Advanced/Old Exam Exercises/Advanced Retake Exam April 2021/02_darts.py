from collections import  deque


def check_points(curr_row, curr_col, multiple):
    row_points = board[curr_row][0] + board[curr_row][-1]
    col_points = board[0][curr_col] + board[-1][curr_col]
    times = 2
    if multiple == "T":
        times = 3
    return (row_points + col_points) * times


SIZE = 7
turns = deque(input().split(", "))

players_info = {}

for player in turns:
    players_info[player] = [501, 0]     # 0 Will keep track on points and 1 will keep track on throws


board = []

for row in range(SIZE):
    r = [int(x) if x.isnumeric() else x for x in input().split()]
    board.append(r)

while True:
    curr_player = turns[0]
    players_info[curr_player][1] += 1
    turns.rotate(1)

    throw_row, throw_col = map(int, input().strip("()").split(", "))

    if 0 <= throw_row < SIZE and 0 <= throw_col < SIZE:

        if board[throw_row][throw_col] == "B":
            print(f"{curr_player} won the game with {players_info[curr_player][1]} throws!")
            break

        elif type(board[throw_row][throw_col]) == int:
            players_info[curr_player][0] -= board[throw_row][throw_col]

        else:
            multiplier = board[throw_row][throw_col]
            points = check_points(throw_row, throw_col, multiplier)
            players_info[curr_player][0] -= points

        if players_info[curr_player][0] <= 0:
            print(f"{curr_player} won the game with {players_info[curr_player][1]} throws!")
            break
