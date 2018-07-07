from random import randint


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.size = 1

    def __str__(self):
        return str(self.data)

    def get_random_node(self):
        n = randint(0, self.size-1)
        return self.get_nth_node(n)

    def get_nth_node(self, n):
        left_size = self.left.size if self.left else 0
        if n < left_size:
            return self.left.get_nth_node(n)
        elif n == left_size:
            return self
        else:
            return self.right.get_nth_node(n - (left_size + 1))

    def insert_inorder(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.insert_inorder(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.insert_inorder(data)
        self.size += 1

    def find_node(self, data):
        if self.data == data:
            return self
        elif data <= self.data:
            return self.left.find_node(data) if self.left else None
        elif data > self.data:
            return self.right.find_node(data) if self.right else None
        return None


if __name__ == '__main__':
    node = BSTNode(20)
    values = [10, 30, 5, 15, 35, 3, 7, 17]
    for data in values:
        node.insert_inorder(data)
    for i in range(40):
        print node.get_random_node().data
