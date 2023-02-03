initial_list = input().split()
initial_list = [int(x) for x in initial_list]

command = input().split()

while command[0] != "end":

    if command[0] == "exchange":
        idx = int(command[1])
        if 0 <= idx < len(initial_list):
            initial_list = initial_list[idx + 1:] + initial_list[: idx + 1]
        else:
            print(f"Invalid index")

    elif command[0] == "max":
        instruction = command[1]
        even = [x for x in initial_list if x % 2 == 0]
        odd = [x for x in initial_list if x % 2 != 0]
        if instruction == "even" and even:
            if initial_list.count(max(even)) == 1:
                print(f"{initial_list.index(max(even))}")
            else:
                print((len(initial_list) - initial_list[::-1].index(max(even)) - 1))
        elif instruction == "odd" and odd:
            if initial_list.count(max(odd)) == 1:
                print(f"{initial_list.index(max(odd))}")
            else:
                print((len(initial_list) - initial_list[::-1].index(max(odd)) - 1))
        else:
            print(f"No matches")

    elif command[0] == "min":
        instruction = command[1]
        even = [x for x in initial_list if x % 2 == 0]
        odd = [x for x in initial_list if x % 2 != 0]
        if instruction == "even" and even:
            if initial_list.count(min(even)) == 1:
                print(f"{initial_list.index(min(even))}")
            else:
                print((len(initial_list) - initial_list[::-1].index(min(even)) - 1))
        elif instruction == "odd" and odd:
            if initial_list.count(min(odd)) == 1:
                print(f"{initial_list.index(min(odd))}")
            else:
                print((len(initial_list) - initial_list[::-1].index(min(odd)) - 1))
        else:
            print(f"No matches")

    elif command[0] == "first":
        counter = int(command[1])
        if counter > len(initial_list):
            print(f"Invalid count")
        else:
            instruction = command[2]
            return_list = []
            if instruction == "even":
                even_list = [x for x in initial_list if x % 2 == 0]
                return_list = even_list[:counter]
            if instruction == "odd":
                odd_list = [x for x in initial_list if x % 2 != 0]
                return_list = odd_list[:counter]
            print(f"{return_list}")

    elif command[0] == "last":
        counter = int(command[1])
        if counter > len(initial_list):
            print(f"Invalid count")
        else:
            instruction = command[2]
            return_list = []
            if instruction == "even":
                even_list = [x for x in initial_list if x % 2 == 0]
                even_list.reverse()
                return_list = even_list[:counter]
                return_list.reverse()
            if instruction == "odd":
                odd_list = [x for x in initial_list if x % 2 != 0]
                odd_list.reverse()
                return_list = odd_list[:counter]
                return_list.reverse()
            print(f"{return_list}")

    command = input().split()

print(initial_list)
