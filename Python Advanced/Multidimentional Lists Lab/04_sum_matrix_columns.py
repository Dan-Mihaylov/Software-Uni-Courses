rows, columns = map(int, input().split(", "))

matrix = list()

for _ in range(rows):
    curr_list = list(map(int, input().split()))
    matrix.append(curr_list)

for column in range(len(matrix[0])):
    total = 0
    for row in range(rows):
        total += matrix[row][column]
    print(total)
