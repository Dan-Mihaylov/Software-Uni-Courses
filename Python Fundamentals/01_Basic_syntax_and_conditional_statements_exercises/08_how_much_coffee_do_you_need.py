
command = input()

coffees = 0

while command != "END":

    if command.lower() == "dog" or command.lower() == "cat" or \
     command.lower() == "coding" or command.lower() == "movie":

        if command.islower():
            coffees += 1
        elif command.isupper():
            coffees += 2

    command = input()

if coffees > 5:
    print(f"You need extra sleep")
else:
    print(f"{coffees}")
