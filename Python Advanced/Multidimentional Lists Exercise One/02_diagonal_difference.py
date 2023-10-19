def create_matrix(size: int):
    mat = []
    for _ in range(size):
        nested_list = [int(x) for x in input().split()]
        mat.append(nested_list)
    return mat


dimension = int(input())

matrix = create_matrix(dimension)
primary = []
secondary = []

for i in range(len(matrix)):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][len(matrix) - 1 -i])

total_diff = abs(sum(primary) - sum(secondary))
print(total_diff)

