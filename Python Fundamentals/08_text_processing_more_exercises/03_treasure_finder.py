import re


def find_matches(text: str):
    regex = r"(?P<name>(?<=\&)[A-Za-z]+(?=\&))|(?P<coordinates>(?<=<)[A-Za-z0-9]+(?=>))"
    pattern = re.compile(regex)
    matches_ = re.finditer(pattern, text)
    return matches_


keys = [int(x) for x in input().split()]
new_text = list()

while True:
    line = input()
    if line == "find":
        break

    temp_text = str()
    k_idx = 0
    for letter in line:
        temp_text += chr(ord(letter) - keys[k_idx])
        k_idx += 1
        if k_idx == len(keys):
            k_idx = 0

    new_text.append(temp_text)

treasure_info = dict()

for line in new_text:
    matches = find_matches(line)
    is_name = True
    name = ""
    for match in matches:
        if is_name:
            name = match.group()
            treasure_info[match.group()] = treasure_info.get(match.group(), "")
            is_name = False
        else:
            treasure_info[name] = match.group()


for treasure, coordinates in treasure_info.items():
    print(f"Found {treasure} at {coordinates}")
