import re

text = input()
pattern = r"(?<=\s_)([A-Z-a-z0-9]+)($|(?=\s))"
matches = re.finditer(pattern, text)

result = list()
for match in matches:
    result.append(match[0])

print(",".join(result))


# (?<=\b_)([A-Z-a-z0-9]+)(?=\s)
# r"(?<=\b_)[A-Za-z0-9]{1,}($|(?=\s))"