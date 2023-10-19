initial_string = input()
numbers_list = [x for x in initial_string if x.isnumeric()]
remaining_string = [x for x in initial_string if x not in numbers_list]
take = [int(numbers_list[x]) for x in range(len(numbers_list)) if x % 2 == 0]
skip = [int(numbers_list[x]) for x in range(len(numbers_list)) if x % 2 != 0]

final_string = []

for idx in range(len(take)):
    i = take[idx]
    while i > 0 and remaining_string:
        final_string += remaining_string.pop(0)
        i -= 1
    j = skip[idx]
    while j > 0 and remaining_string:
        remaining_string.pop(0)
        j -= 1
print(f"".join(final_string))
