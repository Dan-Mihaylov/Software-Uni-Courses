import re

regex = r"\d+"

while True:
    line = input()
    if line:
        matches = re.finditer(regex, line)
        for match in matches:
            print(match[0], end=" ")
    else:
        break

