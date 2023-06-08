def words_sorting(*args):
    words_info = {}
    result = []

    for word in args:
        words_info[word] = 0

        for letter in word:
            words_info[word] += ord(letter)


    sum_values = sum(words_info.values())

    if sum_values % 2 == 1:

        for word, value in dict(sorted(words_info.items(), key=lambda x: -x[1])).items():
            result.append(f"{word} - {value}")

    else:

        for word, value in dict(sorted(words_info.items(), key=lambda x: x[0])).items():
            result.append(f"{word} - {value}")

    return '\n'.join(result)








print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))



