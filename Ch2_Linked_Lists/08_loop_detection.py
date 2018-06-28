from LinkedList import LinkedList


def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:  # no loop
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


if __name__ == '__main__':
    ll = LinkedList([3, 1, 5, 9, 7, 2, 1])
    count = 3
    current = ll.head
    for i in range(count):
        current = current.next
    ll.tail.next = current
    print loop_detection(ll)

