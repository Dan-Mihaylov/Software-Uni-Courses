string_word = input()

words_looking = ["sand", "water", "fish", "sun"]

new_string = string_word.lower()

count = 0

for word in words_looking:
    count += new_string.count(word)

print(count)
