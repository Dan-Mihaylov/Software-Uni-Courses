initial_message = input()

while True:
    line = input()
    if line == "Reveal":
        break

    data = line.split(":|:")
    command = data[0]

    if command == "InsertSpace":
        index = int(data[1])
        initial_message = initial_message[:index] + " " + initial_message[index:]

    elif command == "Reverse":
        substring = data[1]
        if substring in initial_message:
            initial_message = initial_message.replace(substring, "", 1) + substring[::-1]
        else:
            print(f"error")
            continue

    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        if substring in initial_message:
            initial_message = initial_message.replace(substring, replacement)

    print(initial_message)

print(f"You have a new text message: {initial_message}")


