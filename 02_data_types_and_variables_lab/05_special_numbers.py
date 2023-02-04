number = int(input())

special_numbers = [5, 7, 11]

for num in range(1, number + 1):
    cache = (num // 10) + (num % 10)
    if cache in special_numbers:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
