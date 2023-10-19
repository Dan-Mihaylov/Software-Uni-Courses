def item_in_matrix(matrix: list, item: str):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == item:
                return f"({row}, {column})"
    return f"{item} does not occur in the matrix"


size = int(input())
curr_matrix = list()
for _ in range(size):
    curr_list = [*input()]
    curr_matrix.append(curr_list)

look_for = input()

print(item_in_matrix(curr_matrix, look_for))
