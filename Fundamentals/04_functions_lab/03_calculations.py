
def calculate(operator, num1, num2):
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    elif operator == "divide":
        return num1 / num2
    elif operator == "multiply":
        return num1 * num2


operation = input()
a = int(input())
b = int(input())

print(int(calculate(operation, a, b)))
