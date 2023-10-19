characters = input().split(", ")

some_dict = {char: ord(char) for char in characters}

print(some_dict)
