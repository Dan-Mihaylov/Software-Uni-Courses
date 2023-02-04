year = int(input())

while True:
    new_year = str(year + 1)

    year_set = set()

    for digit in new_year:
        year_set.update(digit)

    if len(year_set) == len(new_year):
        print(int(new_year))
        break
    else:
        year += 1
        year_set.clear()

"""
 We are using sets because items in the sets are unique, duplicates are not allowed, so we store the string in the set
 then check if the length of the set is same as the length of the new year, and if it is, it means that all the values
 are unique.
"""