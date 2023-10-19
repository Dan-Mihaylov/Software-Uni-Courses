number = int(input())
bit_position = int(input())

mask = ~(1 << bit_position)
result = mask & number

print(result)

# to destroy the bit at a given position first you have to set it to 0 and all the other bits to 1
# then with the mask & number operator, you convert the rest of the bits to whatever value
# they had, and the one that you needed to destroy to 0

