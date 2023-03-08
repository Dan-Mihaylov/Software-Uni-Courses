words_list = input().split()

emoticon_list = list()

for word in words_list:
    if word.startswith(":") and len(word) <= 3:
        if not word[1:2].isnumeric():
            emoticon_list.append(word[:2])

[print(f"{word}") for word in emoticon_list]
