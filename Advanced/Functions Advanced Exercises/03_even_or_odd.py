def even_odd(*args):

    command = args[-1]
    if command == "even":
        result = list(filter(lambda x: x % 2 == 0, args[:-1]))
        return result

    elif command == "odd":
        result = list(filter(lambda x: x % 2 == 1, args[:-1]))
        return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
