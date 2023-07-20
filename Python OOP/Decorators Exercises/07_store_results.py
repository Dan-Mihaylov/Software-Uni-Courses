class store_results:
    _result = "results.txt"

    def __init__(self, function) -> None:
        self.function = function

    def __call__(self, *args, **kwargs) -> None:
        func_result = self.function(*args)
        func_name = self.function.__name__

        with open(self._result, "a") as file:
            file.write(f"Function '{func_name}' was called. Result: {func_result}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
