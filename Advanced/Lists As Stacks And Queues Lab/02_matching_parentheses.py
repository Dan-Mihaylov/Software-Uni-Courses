class Stack:

    def __init__(self):
        self.stack = []

    def push(self, values):
        self.stack.append(values)

    def pop(self):
        return self.stack.pop()


line = input()
stack = Stack()

for i in range(len(line)):
    if line[i] == "(":
        stack.push(i)
    elif line[i] == ")":
        print(line[stack.pop():i + 1])
