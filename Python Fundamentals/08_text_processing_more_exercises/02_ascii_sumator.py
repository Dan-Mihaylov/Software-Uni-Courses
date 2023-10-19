lower_range = ord(input())
upper_range = ord(input())
chars_to_check = input()

# if lower_range > upper_range:
#     lower_range, upper_range = upper_range, lower_range

total = 0

for char in chars_to_check:
    value = ord(char)

    if lower_range < value < upper_range:
        total += value

print(total)
