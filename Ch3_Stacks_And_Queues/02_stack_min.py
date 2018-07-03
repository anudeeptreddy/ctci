
class Node:
    def __init__(self, value, min_val):
        self.value = value
        self.min_val = min_val


class MinStack:
    def __init__(self):
        self.items = []
        self.min = None

    def __str__(self):
        return ' '.join([str(node.value) for node in self.items])

    def push(self, item):
        if not self.min:  # stack is empty
            self.min = item
        else:  # stack is non empty
            self.min = item if item <= self.min else self.min
        node = Node(item, self.min)
        self.items.append(node)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Cannot pop from an empty stack')
        item = self.items.pop()
        return item

    def top(self):
        if self.is_empty():
            raise RuntimeError('Cannot provide top element in an empty stack')
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def min_value(self):
        return self.top().min_val


if __name__ == '__main__':
    minstack = MinStack()
    minstack.push(5)
    print '%s is min in stack %s' % (minstack.min_value(), minstack)
    minstack.push(6)
    print '%s is min in stack %s' % (minstack.min_value(), minstack)
    minstack.push(3)
    print '%s is min in stack %s' % (minstack.min_value(), minstack)
    minstack.push(7)
    print '%s is min in stack %s' % (minstack.min_value(), minstack)
    minstack.pop()
    print '%s is min in stack %s' % (minstack.min_value(), minstack)
    minstack.pop()
    print '%s is min in stack %s' % (minstack.min_value(), minstack)


# o/p:
# 5 is min in stack 5
# 5 is min in stack 5 6
# 3 is min in stack 5 6 3
# 3 is min in stack 5 6 3 7
# 3 is min in stack 5 6 3
# 5 is min in stack 5 6
