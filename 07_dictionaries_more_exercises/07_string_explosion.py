initial_string = input()
result_string = str()
carry = 0
explosion = False

for value in initial_string:
    if value == ">":
        explosion = True
    elif explosion:
        carry += int(value) - 1
        explosion = False
        continue
    elif carry != 0:
        carry -= 1
        continue
    result_string += value
print(result_string)
