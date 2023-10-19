rows, columns = map(int, input().split(", "))

matrix = list()

for _ in range(rows):
    curr_list = list(map(int, input().split(", ")))
    matrix.append(curr_list)


def get_max_square(mat: list):
    maximum = 0
    elements = list()

    for row in range(len(mat) - 1):
        next_row = row + 1
        for col in range(len(mat[0]) - 1):
            next_col = col + 1
            one = mat[row][col]
            two = mat[row][next_col]
            three = mat[next_row][col]
            four = mat[next_row][next_col]
            total = one + two + three + four
            if total > maximum:
                maximum = total
                elements = [[str(one), str(two)], [str(three), str(four)]]

    return elements, maximum


block, biggest = get_max_square(matrix)
for nums in block:
    print(f" ".join(nums))
print(biggest)
