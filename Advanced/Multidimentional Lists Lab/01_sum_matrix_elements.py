rows, columns = map(int, input().split(", "))

matrix = list()
for _ in range(rows):
    curr_list = list(map(int, input().split(", ")))
    matrix.append(curr_list)

total = 0

for row in matrix:
    # total += sum(row)
    for element in row:
        total += element

print(total)
print(matrix)
