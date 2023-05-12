iterations = int(input())

content = set()
[[content.add(x) for x in input().split()] for _ in range(iterations)]

# for _ in range(iterations):
#     curr = {content.add(x) for x in input().split()}

[print(x) for x in content]
