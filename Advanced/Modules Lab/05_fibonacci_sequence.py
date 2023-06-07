from fibonacci import create_fibonacci_sequence, locate_number

seq = None

while True:
    command = input().split()
    if command[0] == "Stop":
        break

    if command[0] == "Create":
        count = int(command[-1])
        seq = create_fibonacci_sequence(count)
        print(f" ".join(str(x) for x in seq))

    elif command[0] == "Locate":
        number = int(command[-1])
        print(locate_number(number, seq))

