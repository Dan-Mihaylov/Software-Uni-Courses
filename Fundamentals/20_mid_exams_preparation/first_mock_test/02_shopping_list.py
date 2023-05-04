
groceries = input().split("!")
line = input()

while line != "Go Shopping!":
    line = line.split()
    command = line[0]
    item = line[1]
    if command == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif command == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif command == "Correct":
        new_item = line[2]
        if item in groceries:
            idx = groceries.index(item)
            groceries[idx] = new_item
    elif command == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    line = input()

print(f", ".join(groceries))
