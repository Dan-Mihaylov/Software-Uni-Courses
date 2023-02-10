numbers_list = [int(x) for x in input().split(", ")]
# indexes_list = [numbers_list.index(x) for x in numbers_list if x % 2 == 0]
# print(indexes_list)   # If the numbers are the same it will return the index of the first time

# You map the object to contain the index, or a string "no"
found_indices_or_no = map(
    lambda x: x if numbers_list[x] % 2 == 0 else "no",
    range(len(numbers_list))
)
# then you iterate over the mapped object and filter out the string no, all this in a created list.
even_indices = list(filter(lambda a: a != "no", found_indices_or_no))
print(even_indices)

