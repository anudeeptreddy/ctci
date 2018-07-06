# TRAVERSAL HELPER


def in_order_traversal(root):
    if not root:
        return None
    in_order_traversal(root.left)
    print root.data
    in_order_traversal(root.right)


# SOLUTION O(tree depth)- USING DEPTH CALCULATION


def get_depth(node):
    depth = 0
    while node.parent:
        node = node.parent
        depth += 1
    return depth


def first_common_ancestor(node1, node2):
    # first common ancestor with link to parent
    if not node1 or not node2:
        return None

    node1_depth, node2_depth = get_depth(node1), get_depth(node2)
    deep, short = (node1, node2) if node1_depth >= node2_depth else (node2, node1)
    depth_diff = abs(node1_depth-node2_depth)

    # skip extra difference
    for i in range(depth_diff):
        deep = deep.parent

    # start comparing the parents from same depth
    while deep and short:
        if deep.parent == short.parent:
            return deep.parent
        deep, short = deep.parent, short.parent

    return None


# OPTIMIZED SOLUTION: BY CHECKING IF THE PARENT OF NODE 1 COVERS NODE 2


def get_sibling(node):
    # Get sibling of a node with parent pointers
    if node is None or node.parent is None:
        return None
    parent = node.parent
    return parent.left if parent.right == node else parent.right


def covers(root, node):
    # Search for node in root tree. Return True if found
    if not root: return False
    if root == node: return True    # found
    return covers(root.left, node) or covers(root.right, node)


def common_ancestor_optimized(root, node1, node2):
    # Bases cases: node1 & node2 are in tree or either of the nodes cover each other
    if not covers(root, node1) or not covers(root, node2):  # nodes do not exist in tree
        return None
    if covers(node1, node2):                                # node1 is parent of node2
        return node1
    if covers(node2, node1):                                # node2 is parent of node1
        return node2

    # Travel upwards until you find a node that covers node2
    parent = node1.parent
    sibling = get_sibling(node1)                            # Get sibling of node1
    while not covers(sibling, node2):                       # search for node in sibling tree
        sibling = get_sibling(parent)
        parent = parent.parent

    return parent


# START


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if self.left: self.left.parent = self
        if self.right: self.right.parent = self

    def add_children(self, left=None, right=None):
        self.left, self.right = left, right
        if self.left: self.left.parent = self
        if self.right: self.right.parent = self


if __name__ == '__main__':
    items = ['a', 'b', 'c', 'd', 'e', 'f']
    nodes = {}
    for val in items:
        nodes[val] = TreeNode(val)
    nodes['a'].add_children(nodes['b'], nodes['c'])
    nodes['b'].add_children(nodes['d'], nodes['e'])
    nodes['d'].add_children(nodes['f'], None)
    T = nodes['a']
    print first_common_ancestor(nodes['f'], nodes['e']).data
    print common_ancestor_optimized(T, nodes['f'], nodes['e']).data


# o/p:
# b
