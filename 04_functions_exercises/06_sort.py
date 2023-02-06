def sorted_list(initial_list):
    numbers_list = [int(x) for x in initial_list]
    return sorted(numbers_list)


initial_input = input().split()
print(sorted_list(initial_input))
