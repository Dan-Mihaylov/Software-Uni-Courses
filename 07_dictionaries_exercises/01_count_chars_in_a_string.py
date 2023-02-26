input_line = input()
dictionary = {}

for letter in input_line:
    if letter != " ":
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
