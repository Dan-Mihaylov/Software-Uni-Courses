code_list = input().split()
for code in code_list:
    digits = ""
    remaining_letters = ""
    for character in code:
        if character.isnumeric():
            digits += character
        else:
            remaining_letters += character
    if len(remaining_letters) > 1:
        decoded_word = chr(int(digits)) + remaining_letters[-1:] + remaining_letters[1:-1] + remaining_letters[0]
    else:
        decoded_word = chr(int(digits)) + remaining_letters[-1:] + remaining_letters[1:-1]
    print(f"{decoded_word}", end=" ")
