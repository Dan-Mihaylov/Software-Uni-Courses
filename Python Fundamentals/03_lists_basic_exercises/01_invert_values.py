values = input().split()

inverted_values = []

for element in values:
    curr_num = -int(element)
    inverted_values.append(curr_num)

print(inverted_values)

"""
values = input().split()        # We have it as strings

inverted_values = []

for value in values:

    if int(value) < 0:          # Every time I use the value have to convert to int
        inverted_values.append(abs(int(value)))

    elif int(value) >= 0:
        inverter = int(value) - int(value) * 2
        inverted_values.append(inverter)

print(inverted_values)
"""