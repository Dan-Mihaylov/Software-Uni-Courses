import unittest


class Stack:

    def __init__(self):
        self.data = []

    def push(self, element: str):
        if type(element) == str:
            self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()