import re

text = input()

regex = r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))"
pattern = re.compile(regex)
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
