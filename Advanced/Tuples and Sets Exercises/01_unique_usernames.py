iterations = int(input())

usernames = set()

for _ in range(iterations):
    name = input()
    usernames.add(name)

[print(x) for x in usernames]
