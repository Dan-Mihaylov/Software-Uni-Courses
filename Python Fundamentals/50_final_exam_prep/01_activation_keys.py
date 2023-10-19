initial_key = input()

line = input()

while line != "Generate":
    data = line.split(">>>")
    command = data[0]

    if command == "Contains":
        substring = data[1]
        if substring in initial_key:
            print(f"{initial_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        case = data[1]
        start_idx = int(data[2])
        end_idx = int(data[3])
        first_half = initial_key[:start_idx]
        changing_part = initial_key[start_idx:end_idx]
        last_part = initial_key[end_idx:]
        if case == "Upper":
            initial_key = first_half + changing_part.upper() + last_part
        elif case == "Lower":
            initial_key = first_half + changing_part.lower() + last_part
        print(initial_key)

    elif command == "Slice":
        start_idx = int(data[1])
        end_idx = int(data[2])
        initial_key = initial_key[:start_idx] + initial_key[end_idx:]
        print(initial_key)

    line = input()

print(f"Your activation key is: {initial_key}")
