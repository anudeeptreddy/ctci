def validate_bst(root, left_bound, right_bound):
    if not root:
        return True
    return left_bound < root.data <= right_bound and \
        validate_bst(root.left, left_bound, root.data) and \
        validate_bst(root.right, root.data, right_bound)


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3)), TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)))
    print validate_bst(tree, float('-inf'), float('inf'))
