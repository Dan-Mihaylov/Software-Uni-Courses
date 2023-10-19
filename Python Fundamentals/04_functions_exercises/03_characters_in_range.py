def char_in_range(start, end):
    for digit in range(start + 1, end):
        character = chr(digit)
        print(f"{character}", end=" ")


char_one = input()
char_two = input()

start_range = ord(char_one)
end_range = ord(char_two)
char_in_range(start_range, end_range)
