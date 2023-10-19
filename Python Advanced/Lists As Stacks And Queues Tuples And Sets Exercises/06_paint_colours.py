from collections import deque

colours = deque(input().split())

secondary_colours = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"},
}

available_colours = {"yellow", "green", "red", "purple", "blue", "orange"}
result = []

while colours:
    first = colours.popleft()
    second = colours.pop() if colours else ""   # if there is a colour we will pop it if no we will have empty string
    curr_colour = {first + second, second + first}

    for col in curr_colour:
        if col in available_colours:
            result.append(col)
            break
    else:
        for col in (first, second):
            if len(col) > 1:
                colours.insert(len(colours) // 2, col[:-1])

for colour in result:
    if colour in secondary_colours.keys():
        if not secondary_colours[colour].issubset(result):
            result.remove(colour)

print(result)
