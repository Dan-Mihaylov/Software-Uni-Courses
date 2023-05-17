def check_coordinates(mat: list, coordinates: list):   # Give a list with the x, y coordinate
    for coo in coordinates:
        if coo not in range(len(mat)):
            return False
    return True


rows = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(rows)]

line = input()

while line != "END":
    command, *indices, value = line.split()
    indices = [int(x) for x in indices]
    row, col = indices
    value = int(value)

    if check_coordinates(matrix, indices):

        if command == "Add":
            matrix[row][col] += value

        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print(f"Invalid coordinates")

    line = input()

[print(*x) for x in matrix]

