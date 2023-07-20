from functools import wraps

def multiply(times):    # The decorator creator takes an argument, which you can use to perform actions

    def decorator(function):

        @wraps(function)    # You use the @wraps to keep the original functions .__doc__ (String documentation)
        def wrapper(parameter):     # Here you can pass another argument to the function you are wrapping
            result = function(parameter)
            return result * times

        return wrapper  # The decorator should return the wrapper function

    return decorator    # The Decorator creator func should return the decorator



@multiply(3)    # You can pass the argument to execute on an inner function in the decorator wrapper
def add_ten(number):    # This argument will be passed from the calling of the add_ten function.
    """ This is some documentation, that will not have to be lost"""
    return number + 10

print(add_ten(3))
print(add_ten.__doc__)


@multiply(10)
def add_ten(number):
    return number + 10

print(add_ten(5))
