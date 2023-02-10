initial_string = input()
vowels = ["a", "o", "u", "e", "i"]
no_vowels = [x for x in initial_string if x.lower() not in vowels]
print(f"".join(no_vowels))
