phonebook = dict()

input_line = input()

while "-" in input_line:
    name, number = input_line.split("-")
    phonebook[name] = phonebook.get(name, "")
    phonebook[name] = number
    input_line = input()

iterations = int(input_line)

for i in range(iterations):
    contact = input()
    if contact in phonebook:
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")

