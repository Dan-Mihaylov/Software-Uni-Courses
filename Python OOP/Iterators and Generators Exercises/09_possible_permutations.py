from itertools import permutations


def possible_permutations(seq: list):
    result = permutations(seq)

    for item in result:
        yield list(item)


# [print(n) for n in possible_permutations([1, 2, 3])]
# [print(n) for n in possible_permutations([1])]

