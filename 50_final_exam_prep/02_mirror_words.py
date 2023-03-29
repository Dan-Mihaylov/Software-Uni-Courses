import re

line = input()

pairs_count = 0
word_match = list()     # 0 idx will be word 1, 1 idx will be word 2

regex = r"([@#])(?P<one>[A-Za-z]{3,})\1\1(?P<two>[A-Za-z]{3,})\1"
pattern = re.compile(regex)
matches = re.finditer(pattern, line)
for match in matches:
    pairs_count += 1
    word_1 = match["one"]
    word_2 = match["two"]
    if word_1 == word_2[::-1]:
        word_match.append(f"{word_1} <=> {word_2}")

if pairs_count == 0:
    print(f"No word pairs found!")
else:
    print(f"{pairs_count} word pairs found!")
if not word_match:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(word_match))

