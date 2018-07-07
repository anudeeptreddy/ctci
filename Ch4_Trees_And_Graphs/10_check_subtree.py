
def is_equal(T, t):
    if T is None and t is None:
        return True
    elif T is None or t is None:
        return False
    elif T.data != t.data:
        return False
    else:
        return is_equal(T.left, t.left) and is_equal(T.right, t.right)


def is_subtree(T, t):
    if t is None:                               # empty subtree is always a subtree of any tree
        return True
    elif T is None and t is not None:           # big tree is none & small tree exists
        return False
    elif T.data == t.data and is_equal(T, t):   # when a node equal to t is found in T, verify if the trees are equal
        return True
    return is_subtree(T.left, t) or is_subtree(T.right, t)  # check for t in left & right sub trees


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
    big_tree_nodes = ['a', 'b', 'c', 'd', 'e']
    small_tree_nodes = ['b', 'd', 'e']
    big_tree = {}
    small_tree = {}
    for val in big_tree_nodes:
        big_tree[val] = TreeNode(val)
    for val in small_tree_nodes:
        small_tree[val] = TreeNode(val)

    big_tree['a'].add_children(big_tree['b'], big_tree['c'])
    big_tree['b'].add_children(big_tree['d'], big_tree['e'])
    small_tree['b'].add_children(small_tree['d'], small_tree['e'])
    # small_tree['e'].add_children(TreeNode('quit'))

    T = big_tree['a']
    t = small_tree['b']

    print is_subtree(T, t)
