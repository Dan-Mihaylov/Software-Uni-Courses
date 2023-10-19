integer_list = [int(x) for x in input().split(", ")]

positive = list(filter((lambda x: x >= 0), integer_list))
negative = list(filter((lambda x: x < 0), integer_list))
even = list(filter((lambda x: x % 2 == 0), integer_list))
odd = list(filter((lambda x: x % 2 != 0), integer_list))

print(f"Positive:", end=" ")
print(f", ".join([str(x) for x in positive]))
print(f"Negative:", end=" ")
print(f", ".join([str(x) for x in negative]))
print(f"Even:", end=" ")
print(f", ".join([str(x) for x in even]))
print(f"Odd:", end=" ")
print(f", ".join([str(x) for x in odd]))

"""
integer_list = [str(x) for x in integer_list]
print(f"Positive: {', '.join([x for x in integer_list if int(x) >= 0])}")
"""

# This can be done with for cycle rather than list comprehension to make it  more efficient, since for
# cycle will iterate only ones through the list and with if statements segregate the result according
# too the conditions given.
