
n = int(input())

not_pure = [",", ".", "_"]

for _ in range(n):
    string = input()

    for i in not_pure:

        if i in string:
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
