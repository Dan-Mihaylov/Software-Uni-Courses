import re

text = input().upper()
word = input().upper()

regex = r"\b" + word + r"\b"
pattern = re.compile(regex)
matches = re.finditer(pattern, text)

result = 0
for match in matches:
    result += 1

print(result)
