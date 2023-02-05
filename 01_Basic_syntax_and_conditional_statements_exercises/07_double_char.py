
command = input()

while command != "End":

    new_word = ""

    if command != "SoftUni":
        for i in command:
            new_word += i * 2
    else:
        command = input()
        continue

    print(new_word)

    command = input()
