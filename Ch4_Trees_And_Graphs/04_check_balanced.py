
def get_height(tree_node):
    if not tree_node:
        return -1
    return max(get_height(tree_node.left), get_height(tree_node.right)) + 1


def is_balanced(tree_node):
    if not tree_node:   # base case, empty tree is a balance tree
        return True
    height_diff = get_height(tree_node.left) - get_height(tree_node.right)
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(tree_node.left) and is_balanced(tree_node.right)


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


if __name__ == '__main__':
    node_j = TreeNode('J')
    node_i = TreeNode('I', node_j, None)
    node_h = TreeNode('H', node_i, None)
    node_e = TreeNode('E')
    node_d = TreeNode('D')
    node_f = TreeNode('F', node_h, None)
    node_c = TreeNode('C', node_f, None)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lls_list = []   # linked list using built in deque
    print is_balanced(node_a)