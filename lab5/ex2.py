class Queue:
    queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if len(self.queue) == 0:
            return None
        element = self.queue[0]
        self.queue.pop(0)
        return element

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

queue1 = Queue()

queue1.push(1)
queue1.push(2)
queue1.push(3)

print(queue1.peek())

print(queue1.pop())
print(queue1.pop())
print(queue1.pop())

print(queue1.pop())
print(queue1.peek())