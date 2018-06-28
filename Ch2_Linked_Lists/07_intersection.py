from LinkedList import LinkedList


def is_intersection(ll1, ll2):
    if not ll1.head or not ll2.head:
        return None

    if ll1.tail is not ll2.tail:
        return False

    longer = ll1 if len(ll1) > len(ll2) else ll2
    shorter = ll2 if len(ll1) > len(ll2) else ll1

    diff = len(longer) - len(shorter)
    longer_current, shorter_current = longer.head, shorter.head

    for i in range(diff):
        longer_current = longer_current.next

    while longer_current is not shorter_current:
        longer_current = longer_current.next
        shorter_current = shorter_current.next

    return longer_current


if __name__ == '__main__':
    ll1 = LinkedList([3, 1, 5, 9, 7, 2, 1])
    ll2 = LinkedList([4, 6])
    current = ll1.head
    count = 4
    for i in range(count):
        current = current.next
    ll2.tail.next = current
    ll2.tail = ll1.tail
    ll2.length = len(ll2) + (len(ll1) - count)

    print ll1
    print ll2
    print is_intersection(ll1, ll2)

