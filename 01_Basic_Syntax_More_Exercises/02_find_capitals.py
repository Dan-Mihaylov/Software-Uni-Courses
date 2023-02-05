
input_string = input()

capital_letters_indexes = []

for index, letter in enumerate(input_string):
    if letter.isupper():
        capital_letters_indexes.append(index)

print(capital_letters_indexes)