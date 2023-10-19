morse_words = input().split(" | ")

alphabet = {
    ".-": "A", "-...": "B",  "-.-.": "C","-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V",
    ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"
}

converted_words = list()

for word in morse_words:
    letters = word.split()
    temp = str()
    for letter in letters:
        if letter in alphabet:
            temp += alphabet[letter]
    converted_words.append(temp)

print(f" ".join(converted_words))
