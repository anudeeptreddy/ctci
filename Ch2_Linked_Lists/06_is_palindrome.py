from LinkedList import LinkedList


def is_palindrome(ll):
    if ll.head is None:
        return None

    stack = []
    slow = fast = ll.head

    while fast and fast.next:   # when fast reached end of ll, slow will be at mid point of ll
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:   # odd number of elements
        slow = slow.next   # hence skip the middle element

    while slow:
        if slow.value != stack.pop():
            break
        return True
    return False


if __name__ == '__main__':
    ll = LinkedList([3, 2, 5, 2, 3])
    print ll
    print is_palindrome(ll)

