def insert_el(initial_list, el, times):
    middle = len(initial_list) // 2
    for _ in range(times):
        new = f"-{el}a"
        initial_list.insert(middle, new)
    return initial_list


elements_list = [x for x in input().split()]

moves = 0
has_won = False
command = input()

while command != "end" and not has_won:
    command = command.split()
    moves += 1
    index_1 = int(command[0])
    index_2 = int(command[1])

    if index_1 == index_2 or index_1 not in range(len(elements_list)) \
       or index_2 not in range(len(elements_list)):
        elements_list = insert_el(elements_list, moves, 2)
        print("Invalid input! Adding additional elements to the board")

    elif elements_list[index_1] == elements_list[index_2]:
        element = elements_list[index_1]
        print(f"Congrats! You have found matching elements - {element}!")
        [elements_list.remove(element) for x in range(2)]
        if len(elements_list) == 0:
            print(f"You have won in {moves} turns!")
            has_won = True

    elif elements_list[index_1] != elements_list[index_2]:
        print(f"Try again!")

    command = input()

if not has_won:
    print(f"Sorry you lose :(")
    print(f" ".join(elements_list))


