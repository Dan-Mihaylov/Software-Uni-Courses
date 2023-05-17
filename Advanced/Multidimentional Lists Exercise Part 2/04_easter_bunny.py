field = [[int(x) if x.isnumeric() else x for x in input().split()] for _ in range(int(input()))]


def go_up(mat: list, bunny_pos: list):  # rows must decrease
    total = 0
    row, col = bunny_pos
    path = []
    while row - 1 in range(len(mat)):
        row -= 1
        if mat[row][col] == "X":
            break
        total += mat[row][col]
        path.append([row, col])
    return ["up", path, total]


def go_down(mat: list, bunny_pos: list):    # rows must increase
    total = 0
    row, col = bunny_pos
    path = []
    while row + 1 in range(len(mat)):
        row += 1
        if mat[row][col] == "X":
            break
        total += mat[row][col]
        path.append([row, col])
    return ["down", path, total]


def go_left(mat: list, bunny_pos: list):    # cols must decrease
    total = 0
    row, col = bunny_pos
    path = []
    while col - 1 in range(len(mat)):
        col -= 1
        if mat[row][col] == "X":
            break
        total += mat[row][col]
        path.append([row, col])
    return ["left", path, total]


def go_right(mat: list, bunny_pos: list):   # cols must increase
    total = 0
    row, col = bunny_pos
    path = []
    while col + 1 in range(len(mat)):
        col += 1
        if mat[row][col] == "X":
            break
        total += mat[row][col]
        path.append([row, col])
    return ["right", path, total]


for row in range(len(field)):

    for col in range(len(field)):
        if field[row][col] == "B":  # Finding the bunny
            up = go_up(field, [row, col])
            down = go_down(field, [row, col])
            right = go_right(field, [row, col])
            left = go_left(field, [row, col])
            best = sorted([up, down, right, left], key=lambda x: -x[-1])

winner = best[0]
direction, path, total = winner
if total > 0:
    print(f"{direction}")
    for p in path:
        print(p)
    print(total)

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# 3
# X X X
# X B X
# X X X