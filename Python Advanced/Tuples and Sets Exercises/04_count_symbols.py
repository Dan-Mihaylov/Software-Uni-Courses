text = input()

char_counter = {}

for char in text:
    char_counter[char] = char_counter.get(char, 0)
    char_counter[char] += 1

for char, times in sorted(char_counter.items()):
    print(f"{char}: {times} time/s")
