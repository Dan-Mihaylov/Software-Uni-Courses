class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def get_max(self):
        return max(self.stack)

    def get_min(self):
        return min(self.stack)


iterations = int(input())
my_stack = Stack()

for _ in range(iterations):

    line = input().split()
    order = int(line[0])

    if order == 1:
        number = int(line[1])
        my_stack.push(number)
    elif order == 2:
        if my_stack.stack:
            my_stack.pop()
    elif order == 3:
        if my_stack.stack:
            print(my_stack.get_max())
    elif order == 4:
        if my_stack.stack:
            print(my_stack.get_min())

data = [str(my_stack.pop()) for i in range(len(my_stack.stack))]
print(f", ".join(data))

# print(*some_list, sep=",")