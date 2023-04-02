initial_spell = input()

while True:
    line = input()
    if line == "Abracadabra":
        break
    data = line.split()
    command = data[0]

    if command == "Abjuration":
        initial_spell = initial_spell.upper()
        print(initial_spell)

    elif command == "Necromancy":
        initial_spell = initial_spell.lower()
        print(initial_spell)

    elif command == "Illusion":
        index = int(data[1])
        letter = data[2]
        if index in range(len(initial_spell)):
            initial_spell = initial_spell[:index] + letter + initial_spell[index + 1:]
            print("Done!")
        else:
            print(f"The spell was too weak.")

    elif command == "Divination":
        first = data[1]
        second = data[2]
        if first in initial_spell:
            initial_spell = initial_spell.replace(first, second)
            print(initial_spell)

    elif command == "Alteration":
        substring = data[1]
        if substring in initial_spell:
            initial_spell = initial_spell.replace(substring, "")
            print(initial_spell)

    else:
        print(f"The spell did not work!")

