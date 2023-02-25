iterations = int(input())

dictionary = {}

for _ in range(iterations):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = []

    dictionary[word].append(synonym)


for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
