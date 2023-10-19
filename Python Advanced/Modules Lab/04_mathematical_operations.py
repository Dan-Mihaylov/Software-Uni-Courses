from operator import add, sub, truediv, mul, pow


def operations(*args):
    first_number, operator, second_number = args
    first_number = float(first_number)
    second_number = int(second_number)

    operations_ = {
        "*": mul(first_number, second_number),
        "^": pow(first_number, second_number),
        "/": truediv(first_number, second_number),
        "+": add(first_number, second_number),
        "-": sub(first_number, second_number),
    }
    return f"{operations_[operator]:.2f}"


print(operations(*input().split()))
