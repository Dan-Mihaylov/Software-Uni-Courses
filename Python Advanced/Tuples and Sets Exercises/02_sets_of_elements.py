n, m = map(int, input().split())

first = {input() for _ in range(n)}
second = {input() for _ in range(m)}

similar = first.intersection(second)
[print(x) for x in similar]
