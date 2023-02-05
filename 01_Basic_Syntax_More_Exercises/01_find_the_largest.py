number = input()

num_list = []

for i in number:
    num_list.append(int(i))

num_list.sort()
num_list.reverse()

for i in num_list:
    print(i, end="")
