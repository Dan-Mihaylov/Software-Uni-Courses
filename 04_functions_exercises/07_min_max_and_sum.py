initial_input = input().split()
numbers_list = [int(x) for x in initial_input]

minimum = lambda x: min(x)
maximum = lambda  x: max(x)
summary = lambda x: sum(x)

print(f"The minimum number is {minimum(numbers_list)}")
print(f"The maximum number is {maximum(numbers_list)}")
print(f"The sum number is: {summary(numbers_list)}")
