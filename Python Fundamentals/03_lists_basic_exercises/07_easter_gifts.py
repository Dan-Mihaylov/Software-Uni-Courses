gift_list = input().split()
command = input()

while command != "No Money":
    command = command.split()

    if command[0] == "OutOfStock":
        for index in range(len(gift_list)):
            if command[1] == gift_list[index]:
                gift_list[index] = "None"
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gift_list) - 1:
            gift_list[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gift_list[- 1] = command[1]

    command = input()

result = []

for item in gift_list:
    if item != "None":
        result.append(item)
print(" ".join(result))

# Exercise not written correctly because when you have done 2 iterations and it gives you the command "OutOfStock"
# it expects you to iterate over the gifts you have ALREADY bought and if they are the same as the item that is out
# of stock, to change its value to "None" when it should be going to the next items, and check the next occurrence of
# the given item.
