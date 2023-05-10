class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()


initial_input = input()
stack = Stack()

for char in initial_input:
    stack.push(char)

while stack.stack:
    print(stack.pop(), end="")