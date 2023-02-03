
entry = input().split()
nums_to_remove = int(input())
numbers = [int(x) for x in entry]

for _ in range(nums_to_remove):
    numbers.remove(min(numbers))

for i in range(len(numbers)):
    if i != len(numbers) - 1:
        print(f"{numbers[i]}", end=", ")
    else:
        print(numbers[i])

