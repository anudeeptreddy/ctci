
def in_order(bst):
    # in order traversal of a binary search tree
    if not bst:
        return
    in_order(bst.left)
    print bst.data
    in_order(bst.right)


def minimal_height_bst(sorted_array):
    if len(sorted_array) == 0:
        return None
    middle = len(sorted_array) // 2
    left = minimal_height_bst(sorted_array[:middle])    # middle not included
    right = minimal_height_bst(sorted_array[(middle+1):])
    return Node(sorted_array[middle], left, right)


class Node:
    def __init__(self, data, left, right):
        self.data, self.left, self.right = data, left, right


if __name__ == '__main__':
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    bst = minimal_height_bst(sorted_array)
    in_order(bst)
