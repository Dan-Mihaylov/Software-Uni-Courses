string_1, string_2 = input().split()

# Making sure that string_1 is always the longest

if len(string_2) > len(string_1):
    string_1, string_2 = string_2, string_1
result = 0

# I enumerate string one because if it is longer than 2, I can continue and do another operation

for index, letter in enumerate(string_1):
    if index in range(len(string_2)):
        result += ord(letter) * ord(string_2[index])
    else:
        result += ord(letter)

print(result)
