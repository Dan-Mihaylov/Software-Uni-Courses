def is_smallest(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        print(n1)
    elif n2 < n1 and n2 < n3:
        print(n2)
    elif n3 < n1 and n3 < n2:
        print(n3)


num1 = int(input())
num2 = int(input())
num3 = int(input())
is_smallest(num1, num2, num3)
