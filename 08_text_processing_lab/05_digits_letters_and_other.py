word = input()

words_list = [[], [], []]

for ch in word:
    if ch.isnumeric():
        words_list[0].append(ch)
    elif ch.isalpha():
        words_list[1].append(ch)
    else:
        words_list[2].append(ch)

for word_ in words_list:
    print(f"".join(word_))
