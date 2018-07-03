
class ThreeInOneStacks:
    def __init__(self):
        self.stacks = [None, None, None]
        self.stack_top_idx = [0, 1, 2]

    def push(self, stack_num, item):
        if len(self.stacks) <= self.stack_top_idx[stack_num]:
            self.stacks += [None] * len(self.stacks)   # Double stack capacity
        self.stacks[self.stack_top_idx[stack_num]] = item
        self.stack_top_idx[stack_num] += 3

    def pop(self, stack_num):
        if self.stack_top_idx[stack_num] > 3:
            self.stack_top_idx[stack_num] -= 3
        if self.is_empty(stack_num):
            raise RuntimeError('Cannot pop an element from an empty stack')
        item = self.stacks[self.stack_top_idx[stack_num]]
        self.stacks[self.stack_top_idx[stack_num]] = None
        return item

    def is_empty(self, stack_num):
        return self.stacks[self.stack_top_idx[stack_num]] is None


if __name__ == '__main__':
    stacks = ThreeInOneStacks()
    stacks.push(1, 10)
    stacks.push(1, 20)
    stacks.push(2, 10)
    stacks.pop(2)
    stacks.pop(2)
    for i in range(0, len(stacks.stacks), 3):
        print stacks.stacks[i], stacks.stacks[i+1], stacks.stacks[i+2]

