def validate_command(comm: list, mat: list):
    if len(comm) != 5 or comm[0] != "swap":
        return False
    row1 = int(comm[1])
    col1 = int(comm[2])
    row2 = int(comm[3])
    col2 = int(comm[4])
    if row1 not in range(len(mat)) or row2 not in range(len(mat)):
        return False
    elif col1 not in range(len(mat[row1])) or col2 not in range(len(mat[row2])):
        return False
    return True


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    data = command.split()
    if not validate_command(data, matrix):
        print("Invalid input!")
    else:
        ro1, co1, ro2, co2 = [int(x) for x in data[1:]]
        matrix[ro1][co1], matrix[ro2][co2] = matrix[ro2][co2], matrix[ro1][co1]
        [print(*row, sep=" ") for row in matrix]

    command = input()


# Second Solution


# def check_valid_indices(indices: list):
#     return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)
#
#
# def swap_command(command, indices: list):
#     if check_valid_indices(indices) and command == "swap" and len(indices) == 4:
#         row1, col1, row2, col2 = indices
#
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#         print(*[' '.join(r) for r in matrix], sep="\n")
#     else:
#         print("Invalid input!")
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [input().split() for _ in range(rows)]
#
# valid_rows = range(rows)
# valid_cols = range(cols)
#
# while True:
#     command_type, *info = [int(x) if x.isnumeric() else x for x in input().split()]
#
#     if command_type == "END":
#         break
#
#     swap_command(command_type, info)