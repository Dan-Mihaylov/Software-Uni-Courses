import time


"""
To use Classes as Decorators you have to implement the __call__ method in the class,
this way you are going to make it operate like a function and be callable.
"""

class Fibonacci:

    def __init__(self) -> None:
        self.cache: dict = {}

    def __call__(self, n: int):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.cache[n - 1] + self.cache[n - 2]   # Because the n = the sum of previous two nums

        return self.cache[n]


fib = Fibonacci()

for i in range(5):
    print(fib(i))

print(fib.cache)

# The __call__ method gives you the option to call the class as a function,
# If the name of the method is different, you will have to call it with the dot notation.
# In our case we just call the fib instance by fib(n), and giving it the argument.



"""
To make the class as a Decorator, we have to pass the function in the __init__ method, at the beginning and access it
in its __call__ method.
"""


class func_logger:

    _logfile = "out.log"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        t = time.strftime("%H:%M:%S")
        log_string = f"{self.function.__name__} was called at {t}"

        with open(self._logfile, "a") as file:
            file.write(f"{log_string}\n")

        return self.function(*args)


@func_logger
def say_hi(name):
    print(f"Hi {name}")

@func_logger
def say_bye(name):
    print(f"Bye {name}")


say_hi("Gosho")
say_bye("Gosho")
