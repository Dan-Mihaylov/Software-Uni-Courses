def recursive_power(number, power):
    if power == 0:
        return number
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


print(recursive_power(10, 2))
print(recursive_power(10, 100))


# With recursion you always have a base case, where the recursion will exit if it reaches it, and the recursive
# case, where the recursion ill continue going until it reaches the base case.
# Or until it reaches the maximum depth of recursion.