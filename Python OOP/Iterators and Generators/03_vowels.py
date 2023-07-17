class vowels:
    VOWELS = "AEOUIY"

    def __init__(self, characters: str):
        self.characters = characters
        self.vowels = [x for x in self.characters if x.upper() in vowels.VOWELS]
        self.index = -1     # -1, because we increment it BEFORE we return it in the __next__ method.

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.vowels) - 1:
            raise StopIteration

        self.index += 1

        return self.vowels[self.index]


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)