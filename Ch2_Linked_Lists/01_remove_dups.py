
from LinkedList import LinkedList


def remove_dups_hash(ll):
    # O(N) time O(N) space
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.next])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


def remove_dups_runner(ll):
    # O(N**2)
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll


if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(100, 0, 9)
    print ll
    print remove_dups_runner(ll)
