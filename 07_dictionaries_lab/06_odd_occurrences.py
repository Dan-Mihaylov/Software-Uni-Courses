words = input().split()

occurrences = {}

for word in words:
    lowercase_word = word.lower()
    if lowercase_word not in occurrences:
        occurrences[lowercase_word] = 1
    else:
        occurrences[lowercase_word] += 1

for word in occurrences:
    if occurrences[word] % 2 != 0:
        print(word, end=" ")
