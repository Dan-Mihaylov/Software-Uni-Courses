command = input()

# while command != "end":
#     print(f"{command} = {command[::-1]}")
#     command = input()

while command != "end":
    reversed_word = ""
    for character in reversed(command):
        reversed_word += character
    print(f"{command} = {reversed_word}")

    command = input()
    