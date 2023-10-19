# from math import inf
#
# def create_matrix(size: int):
#     mat = []
#     for _ in range(size):
#         nested_list = [int(x) for x in input().split()]
#         mat.append(nested_list)
#     return mat
#
#
# def get_matrix_sum(mat: list):
#     total = 0
#     for r in mat:
#         total += sum(r)
#     return total
#
#
# rows, coll = map(int, input().split())
# matrix = create_matrix(rows)
# max_sum = -inf
# max_matrix = []
#
# for row in range(rows - 2):
#     curr_matrix = []
#     for col in range(coll - 2):
#         for ro in range(3):
#             curr_line = []
#             curr_row = ro + row
#             for curr in range(3):
#                 curr_col = col + curr
#                 curr_line.append(matrix[curr_row][curr_col])
#             curr_matrix.append(curr_line)
#         curr_sum = get_matrix_sum(curr_matrix)
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#             max_matrix = curr_matrix.copy()
#         curr_matrix.clear()
#
# print(f"Sum = {max_sum}")
# for row in max_matrix:
#     print(*row, sep=" ")
#

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float("-inf")
biggest_matrix = []

for row in range(rows - 2):

    for col in range(cols - 2):
        first_rows = matrix[row][col: col + 3]  # use slicing to take all the columns
        second_row = matrix[row + 1][col: col + 3]
        third_row = matrix[row + 2][col: col + 3]

        current_sum = sum(first_rows) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_rows, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*(biggest_matrix[row])) for row in range(3)]

