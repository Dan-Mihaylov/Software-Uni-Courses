import re

line = input()

digit_regex = r"\d"
d_pattern = re.compile(digit_regex)

emoji_regex = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1"
e_pattern = re.compile(emoji_regex)

threshold = 1

numbers = re.finditer(d_pattern, line)
for number in numbers:
    threshold *= int(number.group())

emojis = []

found_emojis = re.finditer(e_pattern, line)
found_counter = 0

for emoji in found_emojis:
    found_counter += 1
    points = 0
    for char in emoji["emoji"]:
        points += ord(char)
    if points >= threshold:
        emojis.append(emoji.group())

print(f"Cool threshold: {threshold}")
print(f"{found_counter} emojis found in the text. The cool ones are:")
for em in emojis:
    print(f"{em}")
