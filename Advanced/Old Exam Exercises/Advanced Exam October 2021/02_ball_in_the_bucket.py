def check_points(c):
    all_columns = [field[i][c] for i in range(SIZE)]
    points = sum(all_columns)
    return points

SIZE = 6
THROWS = 3

field = [[int(x) if x.isnumeric() else x for x in input().split()]for _ in range(SIZE)]

total_points = 0

for _ in range(THROWS):
    row, col = [int(x) for x in input().strip("()").split(", ")]

    if 0 <= row < SIZE and 0 <= col < SIZE:
        if field[row][col] == "B":
            field[row][col] = 0
            total_points += check_points(col)

win = None

if total_points < 100:
    needed = 100 - total_points
    print(f"Sorry! You need {needed} points more to win a prize.")
elif 100 <= total_points < 200:
    win = "Football"
elif 200 <= total_points < 300:
    win = "Teddy Bear"
elif 300 <= total_points:
    win = "Lego Construction Set"

if win:
    print(f"Good job! You scored {total_points} points, and you've won {win}.")