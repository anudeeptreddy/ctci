
def next_node(tree, node):
    # given tree is a bst
    if not tree:
        return None
    # if right sub tree exists => parent is left most node of the right subtree
    child = node.right
    if child:
        while child.left:
            child = child.left
        return child

    # else: parent node is the next node of current node Note: root doesn't have a parent node
    return node.parent if node.parent else None


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if self.left: self.left.parent = self
        if self.right: self.right.parent = self

    def __call__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if self.left: self.left.parent = self
        if self.right: self.right.parent = self

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    node = TreeNode(2, None, None)
    tree = TreeNode(4, node(2, TreeNode(1, None, None), TreeNode(3)), TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)))
    print next_node(tree, node)
