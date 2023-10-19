
word_1 = input()
word_2 = input()

for i in range(len(word_1)):
    if word_1[i] != word_2[i]:
        current_word = word_2[:i + 1] + word_1[i + 1:]
        print(current_word)

