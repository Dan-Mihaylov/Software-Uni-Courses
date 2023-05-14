class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()


numbers = [int(x) for x in input().split()]
my_stack = Stack()
# populating the stack
for num in numbers:
    my_stack.push(num)

[print(my_stack.pop(), end=" ") for i in range(len(my_stack.stack))]
