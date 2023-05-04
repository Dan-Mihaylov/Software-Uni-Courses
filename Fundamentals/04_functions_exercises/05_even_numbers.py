# def return_even_list(list_of_numbers):
#     result = []
#     for i in list_of_numbers:
#         if i % 2 == 0:
#             result.append(i)
#     return result
#
#
# initial_input = input().split()
# numbers_list = [int(x) for x in initial_input]
# print(return_even_list(numbers_list))


def is_even(num):
    return num % 2 == 0


initial_input = input().split()
numbers_list = [int(x) for x in initial_input]
# Use filter, which returns a itterabje object with true or false values, and convert it to list, straight away
# Filter takes a function on which to base the result (True or False) and an iterable.
even_numbers = list(filter(is_even, numbers_list))
print(even_numbers)
