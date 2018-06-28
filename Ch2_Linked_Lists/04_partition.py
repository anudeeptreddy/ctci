from LinkedList import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head
    while current:
        next_node = current.next
        current.next = None
        if current.value < x:   # insert at head using head pointer
            current.next = ll.head
            ll.head = current
        else:   # insert node at tail
            ll.tail.next = current
            ll.tail = current
        current = next_node

    if ll.tail.next is not None:   # self referring node is no node greater than pivot & pivot is 1st element
        ll.tail.next = None


ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
ll = LinkedList([5, 1, 2, 3, 4])
print(ll)
partition(ll, 5)
print(ll)