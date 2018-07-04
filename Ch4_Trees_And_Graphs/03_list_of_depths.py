from collections import deque


def get_depth_list_of_lls(tree_node, lls_list, level):
    if not tree_node:   # base case
        return

    if len(lls_list) == level:      # level not yet in the list
        ll = deque()               # create & add a new ll for this level
        lls_list.append(ll)
    else:                           # level already exists
        ll = lls_list[level]

    ll.append(tree_node)
    get_depth_list_of_lls(tree_node.left, lls_list, level + 1)
    get_depth_list_of_lls(tree_node.right, lls_list, level + 1)


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


if __name__ == '__main__':
    node_h = TreeNode('H')
    node_e = TreeNode('E')
    node_d = TreeNode('D')
    node_f = TreeNode('F', node_h, None)
    node_c = TreeNode('C', node_f, None)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lls_list = []   # linked list using built in deque
    get_depth_list_of_lls(node_a, lls_list, 0)
    for level, ll in enumerate(lls_list):
        print 'nodes in level %s :' % level, ' '.join([x.data for x in ll])


# o/p:
# nodes in level 0 : A
# nodes in level 1 : B C
# nodes in level 2 : D E F
# nodes in level 3 : H

