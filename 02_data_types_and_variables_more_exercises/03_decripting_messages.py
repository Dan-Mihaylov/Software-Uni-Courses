
key = int(input())
lines = int(input())

word = ""

for _ in range(lines):
    letter = input()
    order = ord(letter) + key
    word += (chr(order))

print(word)
