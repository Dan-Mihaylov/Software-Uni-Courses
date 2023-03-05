initial_string = input()

final_string = str()
temp = str()

for letter in initial_string:
    if letter != temp:
        final_string += letter
        temp = letter

print(final_string)
