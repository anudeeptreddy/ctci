from LinkedList import LinkedList


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.append_multiple_values([1, 2, 3, 4])
    middle_node = ll.append(5)
    ll.append_multiple_values([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)