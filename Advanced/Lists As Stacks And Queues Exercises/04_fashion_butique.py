clothes = [int(x) for x in input().split()]
racks = int(input())

counter = 1
capacity = 0

while clothes:
    curr_cloth = clothes.pop()
    if capacity + curr_cloth > racks:
        capacity = curr_cloth
        counter += 1
    else:
        capacity += curr_cloth

print(counter)

# append it in a list and then add the list to the rack, then count the len of the rack