iterations = int(input())

even_set = set()
odd_set = set()

for row in range(1, iterations + 1):
    name = input()
    curr_sum = 0

    for char in name:
        curr_sum += ord(char)

    curr_sum = int(curr_sum / row)

    if curr_sum % 2 == 0:
        even_set.add(curr_sum)
    else:
        odd_set.add(curr_sum)

if sum(even_set) == sum(odd_set):
    union = odd_set.union(even_set)
    print(f", ".join([str(x) for x in union]))
elif sum(even_set) < sum(odd_set):
    difference = odd_set.difference(even_set)
    print(f", ".join([str(x) for x in difference]))
else:
    sym_difference = odd_set.symmetric_difference(even_set)
    print(f", ".join([str(x) for x in sym_difference]))


