number = int(input())
number = number >> 1
num_one_pos = number & 1
print(num_one_pos)

# Looking for the bit in position one.
# We move the bit to the right once with the >> operator
# Then we use a mask 1 and the & operator to find out what bit it is there
# 0 & 0 == 0, 0 & 1 == 0, 1 & 1 == 1

