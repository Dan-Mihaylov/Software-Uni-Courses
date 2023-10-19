# There wont be a case where the cookie is on the border of the matrix, so no need to validate, just
# distribute the presents, up, down, right, left

def eat_cookie(presents_left, nice_kids):
    for x, y in directions.values():
        r = santa_pos[0] + x
        c = santa_pos[1] + y

        if neighbourhood[r][c] in "XV":
            if neighbourhood[r][c] == "V":
                nice_kids += 1

            neighbourhood[r][c] = "-"   # if you visit the kid once, then dont visit again.
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighbourhood = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()

    neighbourhood.append(line)

    if "S" in line:
        santa_pos = [row, line.index("S")]
        neighbourhood[row][santa_pos[1]] = "-"

    total_nice_kids += line.count("V")  # Check how many nice kids are there on the line

command = input()

while command != "Christmas morning":

    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = "S"

if not presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")