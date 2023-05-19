rows, cols = (int(x) for x in input().split())

matrix = []

for row in range(97, 97 + rows):
    curr_list = []

    for col in range(cols):
        first_last = chr(row)
        middle = chr(row + col)
        curr_list.append(first_last + middle + first_last)
    matrix.append(curr_list)

# Solution 2

# for curr in matrix:
#     print(*curr, sep=" ")
#
# rows, cols = [int(x) for x in input().split()]
#
# start = ord("a")
#
# for row in range(start, start + rows):
#     for col in range(cols):
#         print(f"{chr(row)}{chr(row + col)}{chr(row)}", end=" ")
#     print("")
#
