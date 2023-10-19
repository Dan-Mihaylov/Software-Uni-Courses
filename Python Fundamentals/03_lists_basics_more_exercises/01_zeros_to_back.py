initial_list = input().split(", ")
integer_list = [int(x) for x in initial_list]

iterations = integer_list.count(0)

for i in range(iterations):
    index = integer_list.index(0)
    integer_list.append(integer_list.pop(index))

print(integer_list)
