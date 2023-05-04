def sum_numbers(n1, n2):
    result = n1 + n2
    return result


def subtract(diff_first, n3):
    result = diff_first - n3
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(f"{subtract(sum_numbers(num1, num2), num3)}")
