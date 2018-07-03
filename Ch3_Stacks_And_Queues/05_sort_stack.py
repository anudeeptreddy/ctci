class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ' '.join([str(x) for x in self.items])

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

    def sort_stack(self):
        temp_stack = Stack()
        while not self.is_empty():
            # Insert each element in current stack into temp_stack in sorted order
            tmp = self.pop()
            while not temp_stack.is_empty() and temp_stack.peek() > tmp:
                self.push(temp_stack.pop())
            temp_stack.push(tmp)

        # Copy the elements from temp_stack back into current stack
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(4)
    stack.push(3)
    stack.push(5)
    print stack
    stack.sort_stack()
    print stack


# o/p:
#
# 1 2 4 3 5
# 5 4 3 2 1
