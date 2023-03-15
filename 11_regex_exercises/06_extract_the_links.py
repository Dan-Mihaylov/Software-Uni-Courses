import re


regex = r"(www\.)([A-Z-a-z0-9]+)(\.{1})([a-z]+)([\.a-z]*)"
pattern = re.compile(regex)
found_links = list()
while True:
    text = input()

    if text:
        matches = re.finditer(pattern, text)
        for match in matches:
            found_links.append(match.group())
    else:
        break

print(f"\n".join(found_links))
