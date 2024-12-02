class Stack:
    index = 0
    stack = []

    def push(self, value):
        self.stack.append(value)
        self.index += 1

    def pop(self):
        if self.index == 0:
            return None
        element = self.stack[self.index-1]
        self.stack.pop(self.index-1)
        self.index -= 1
        return element

    def peek(self):
        if self.index == 0:
            return None
        return self.stack[self.index-1]

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)

print(stack1.peek())

print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())

print(stack1.peek())
