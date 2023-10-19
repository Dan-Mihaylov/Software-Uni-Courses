names_list = input().split(", ")
list_sorted = sorted(names_list, key=lambda x: (-len(x), x))  # sorts by the length first and then alphabet.
print(list_sorted)

