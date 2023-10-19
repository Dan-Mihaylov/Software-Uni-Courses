initial_list = input().split()

total = 0
for word in initial_list:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:len(word) - 1])

    if first_letter.isupper():
        total += number / (ord(first_letter) - 64)
    else:
        total += number * (ord(first_letter.upper()) - 64)

    if last_letter.isupper():
        total -= ord(last_letter) - 64
    else:
        total += ord(last_letter.upper()) - 64

print(f"{total:.2f}")
