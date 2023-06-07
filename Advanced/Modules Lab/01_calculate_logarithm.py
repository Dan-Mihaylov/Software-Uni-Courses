from math import log


def calculate_log(arg):
    number, base = arg

    if base == "natural":
        return f"{log(int(number)):.2f}"

    result = log(int(number), int(base))
    return f"{result:.2f}"


print(calculate_log([input() for _ in range(2)]))
