
class StackOfPlates:
    def __init__(self):
        self.stacks = []
        self.stack_limit = 2
        self.current_stack = -1

    def __str__(self):
        stack_elems = []
        for i in range(len(self.stacks)):
            for j in range(len(self.stacks[i])):
                stack_elems.append(self.stacks[i][j])
        return ' '.join(map(str, stack_elems))

    def push(self, item):
        if len(self.stacks) == 0 or len(self.stacks[self.current_stack]) == self.stack_limit:
            self.stacks.append([])  # start a new stack of plates
            self.current_stack += 1
        self.stacks[self.current_stack].append(item)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Cannot pop from an empty plate stack')

        item = self.stacks[self.current_stack].pop()
        if len(self.stacks[self.current_stack]) == 0:
            self.stacks.pop()
            self.current_stack -= 1
        return item

    def pop_from_plate_stack(self, plate_stack):
        if self.is_empty_plate_stack(plate_stack):
            raise RuntimeError('Cannot pop from an empty specified stack')

        item = self.stacks[plate_stack].pop()
        if len(self.stacks[plate_stack]) == 0:
            del self.stacks[plate_stack]
            self.current_stack -= 1
        return item

    def is_empty(self):
        return len(self.stacks) == 0

    def is_empty_plate_stack(self, plate_stack):
        return plate_stack > len(self.stacks) - 1


if __name__ == '__main__':
    stack = StackOfPlates()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print stack
    stack.pop_from_plate_stack(1)
    print stack
    stack.pop()
    print stack
    stack.pop()
    print stack
    stack.pop()
    print stack

