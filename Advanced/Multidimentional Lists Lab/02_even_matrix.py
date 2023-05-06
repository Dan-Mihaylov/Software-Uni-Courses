rows = int(input())

matrix = list()

for _ in range(rows):
    curr_list = list(filter(lambda x: x % 2 == 0, map(int, input().split(", "))))
    # I get an input and split it, then map it to become an integer, later I filter the numbers I got,
    # to be even numbers and create a list out of the remaining numbers, then I add the list to the matrix.
    # This saves me on doing a nested for loop
    matrix.append(curr_list)

print(matrix)

