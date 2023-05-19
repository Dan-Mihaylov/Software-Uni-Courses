def create_matrix(size: int):
    mat = []
    for _ in range(size):
        nested_list = [x for x in input().split()]
        mat.append(nested_list)
    return mat


rows, coll = map(int, input().split())
matrix = create_matrix(rows)
counter = 0

for row in range(rows - 1):

    for col in range(coll - 1):
        one = matrix[row][col]
        two = matrix[row][col + 1]
        three = matrix[row + 1][col]
        four = matrix[row + 1][col + 1]
        if len({one, two, three, four}) == 1:
            counter += 1
print(counter)
