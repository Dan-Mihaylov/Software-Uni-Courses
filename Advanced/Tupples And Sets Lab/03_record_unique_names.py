iterations = int(input())

names = {input() for _ in range(iterations)}
[print(name) for name in names]
