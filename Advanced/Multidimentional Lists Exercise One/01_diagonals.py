def create_matrix(size: int):
    matrix = []
    for _ in range(size):
        nested_list = [int(x) for x in input().split(", ")]
        matrix.append(nested_list)
    return matrix


size = int(input())

primary = []
secondary = []
matrix = create_matrix(size)


for i in range(len(matrix)):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][len(matrix) - 1 - i])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
