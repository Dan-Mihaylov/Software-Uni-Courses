def even_numbers(function):

    def wrapper(numbers):
        res = [x for x in numbers if x % 2 == 0]
        return res

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))

# If you want to extend the functionality of a function with a decorator and that function takes an argument,
# the wrapper function also has to be taking the argument, since you execute the decorator first

