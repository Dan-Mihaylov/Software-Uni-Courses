initial_input = input()
every_symbol = list()

current_char = str()
result = str()
for index, char in enumerate(initial_input):
    if not char.isnumeric():
        current_char += char
        every_symbol.append(char.upper())
    else:
        if index + 1 in range(len(initial_input)) and initial_input[index + 1].isnumeric():
            multiplier = int(char + initial_input[index + 1])
        else:
            multiplier = int(char)

        result += current_char.upper() * multiplier
        current_char = str()

unique_sym = len(set(every_symbol))
print(f"Unique symbols used: {unique_sym}")
print(f"{result}")
