def reverse_text(text: str):

    text = text[::-1]
    index = 0

    while index < len(text):
        yield text[index]

        index += 1


# for char in reverse_text("step"):
#     print(char, end="")
