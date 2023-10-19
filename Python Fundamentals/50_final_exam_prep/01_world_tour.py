initial_string = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    if command[0] == "Add Stop":
        index = int(command[1])
        stop = command[2]
        if index in range(len(initial_string)):
            first_part = initial_string[:index]
            second_part = initial_string[index:]
            initial_string = first_part + stop + second_part

    elif command[0] == "Remove Stop":
        start_idx = int(command[1])
        end_idx = int(command[2])
        if start_idx in range(len(initial_string)) and end_idx in range(len(initial_string)):
            initial_string = initial_string[:start_idx] + initial_string[end_idx + 1:]

    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        if old in initial_string:
            initial_string = initial_string.replace(old, new)

    print(initial_string)

print(f"Ready for world tour! Planned stops: {initial_string}")
