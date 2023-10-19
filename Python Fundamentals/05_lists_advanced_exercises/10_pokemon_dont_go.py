pokemons = input().split()

caught_ones = []
curr_value = 0
while len(pokemons) > 0:
    index = int(input())
    if index < 0:
        curr_value = int(pokemons.pop(0))
        pokemons.insert(0, pokemons[-1])
    elif index > len(pokemons) - 1:
        curr_value = pokemons.pop(-1)
        pokemons.append(pokemons[0])
    else:
        curr_value = int(pokemons.pop(index))

    caught_ones.append(curr_value)
    pokemons = [int(x) + curr_value if curr_value >= int(x) else int(x) - curr_value for x in pokemons]

print(sum(caught_ones))
