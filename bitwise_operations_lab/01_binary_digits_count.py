number, target = [int(input()) for _ in range(2)]
counter = 0
while number != 0:
    if number % 2 == target:
        counter += 1
    number = number // 2

print(counter)
