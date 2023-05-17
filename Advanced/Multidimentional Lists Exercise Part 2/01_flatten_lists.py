matrix = [[int(y) for y in x.split()] for x in input().split("|")]
flattened = [el for sublist in matrix[::-1] for el in sublist]
print(*flattened)
