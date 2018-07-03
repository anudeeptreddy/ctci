class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Cannot pop from an empty stack')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise RuntimeError('Cannot pop from an empty stack')
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class QueueViaStacks:
    def __init__(self):
        self.new_top_stack = Stack()
        self.old_top_stack = Stack()

    def enqueue(self, item):
        self.new_top_stack.push(item)

    def dequeue(self):
        self.shift_stacks()
        return self.old_top_stack.pop()

    def peek(self):
        self.shift_stacks()
        return self.old_top_stack.peek()

    def shift_stacks(self):
        if len(self.old_top_stack) == 0:
            while len(self.new_top_stack):
                self.old_top_stack.push(self.new_top_stack.pop())


if __name__ == '__main__':
    queue = QueueViaStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print queue.peek()
    queue.enqueue(4)
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()


# o/p:
# 1
# 1
# 2
# 3
# 4
