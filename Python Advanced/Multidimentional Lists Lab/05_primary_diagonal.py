size = int(input())

matrix = list()

for _ in range(size):
    curr_list = list(map(int, input().split()))
    matrix.append(curr_list)

total = 0

for i in range(len(matrix)):
    total += matrix[i][i]

print(total)


# Get sum of secondary diagonal

def get_sum_secondary_diagonal(mat: list):
    tot = 0
    for i in range(len(matrix) - 1, -1, -1):
        tot += matrix[i][len(matrix) - 1 - i]
    return tot


def get_sum_of_left_half(mat: list):
    tot = 0
    for row in range(len(matrix)):
        for column in range(row + 1):
            tot += mat[row][column]
    return tot


def get_sum_of_right_half(mat: list):
    tot = 0
    for row in range(len(mat)):
        for column in range(row, len(mat)):
            tot += mat[row][column]
    return tot


print(get_sum_secondary_diagonal(matrix))
print(get_sum_of_left_half(matrix))
print(get_sum_of_right_half(matrix))
