from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {
    "rose": {"r", "o", "s", "e"},
    "tulip": {"t", "u", "l", "i", "p"},
    "lotus": {"l", "o", "t", "u", "s"},
    "daffodil": {"d", "a", "f", "f", "o", "d", "i", "l"}
}

# If len(intersection) == len(words["any"]) then we have a word

letters_found = set()
found = False

while vowels and consonants and not found:
    letters_found.add(vowels.popleft())
    letters_found.add(consonants.pop())

    for word, value in words.items():
        if len(value) == len(letters_found.intersection(value)):
            print(f"Word found: {word}")
            found = True
            break

if not found:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")