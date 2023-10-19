rows = int(input())

matrix = list()
flattened_matrix = list()

for _ in range(rows):
    curr_list = list(map(int, input().split(", ")))
    matrix.append(curr_list)

for row in matrix:
    for element in row:
        flattened_matrix.append(element)

print(flattened_matrix)
