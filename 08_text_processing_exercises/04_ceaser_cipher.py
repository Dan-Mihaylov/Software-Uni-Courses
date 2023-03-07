initial_string = input()

encrypted_string = str()

for char in initial_string:
    encrypted_string += chr(ord(char) + 3)

print(encrypted_string)
