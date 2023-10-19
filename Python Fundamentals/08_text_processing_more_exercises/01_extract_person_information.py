iterations = int(input())

for _ in range(iterations):
    some_string = input()

    name = some_string[some_string.index("@") + 1: some_string.index("|")]
    age = some_string[some_string.index("#") +1: some_string.index("*")]

    print(f"{name} is {age} years old.")
    