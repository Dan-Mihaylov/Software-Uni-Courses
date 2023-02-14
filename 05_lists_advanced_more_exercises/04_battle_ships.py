row_nums = int(input())
grid = list()
for _ in range(row_nums):
    curr_row = [int(x) for x in input().split()]
    grid.append(curr_row)
# coordinates of each hit
hits_input = [x for x in input().split()]

destroyed = 0

for el in hits_input:
    tokens = el.split("-")
    row = int(tokens[0])
    coll = int(tokens[1])
    if grid[row][coll] > 0:
        grid[row][coll] -= 1
        if grid[row][coll] == 0:
            destroyed += 1

print(destroyed)
