from LinkedList import LinkedList


def kth_element_recursion(current, position):
    if current is None:
        return 0, None

    index, kth_value = kth_element_recursion(current.next, position)
    index += 1
    if index == position:
        kth_value = current.value

    return index, kth_value


def kth_element_runner(ll, position):
    if ll.head is None:
        return None

    current = ll.head
    runner = ll.head
    counter = 1
    while current.next:
        counter += 1
        if counter > position:
            runner = runner.next
        current = current.next

    return runner.value if counter >= position else None


if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(20, 1, 20)
    print ll
    print kth_element_recursion(ll.head, 4)[1]
    print kth_element_runner(ll, 4)