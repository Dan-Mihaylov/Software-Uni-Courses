def even_parameters(function):

    def wrapper(*args):

        if all([isinstance(x, int) for x in args]):     # Check if all elements are numbers

            if all([x % 2 == 0 for x in args]):     # Check if all elements are even numbers
                result = function(*args)    # Execute the function, unpack the arguments

                return result

        return f"Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
