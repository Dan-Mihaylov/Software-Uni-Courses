
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)


a = int(input())
b = int(input())

first_fact = factorial(a)
second_fact = factorial(b)

calculation = lambda i, j: i / j
print(f"{calculation(first_fact,second_fact):.2f}")
