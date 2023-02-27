iterations = int(input())

parking_info = dict()

for _ in range(iterations):
    input_line = input().split()
    command = input_line[0]
    name = input_line[1]

    if command == "register":
        numberplate = input_line[2]

        if name not in parking_info:
            parking_info[name] = numberplate
            print(f"{name} registered {numberplate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_info[name]}")

    elif command == "unregister":

        if name not in parking_info:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_info[name]

for name, numberplate in parking_info.items():
    print(f"{name} => {numberplate}")
