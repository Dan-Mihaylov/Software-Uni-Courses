words = input().split()

final_string = ""

# for word in words:
#     for _ in range(len(word)):
#         final_string += word

for word in words:
    length = len(word)
    final_string += word * length

print(final_string)
