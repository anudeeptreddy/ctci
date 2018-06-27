# LinkedList data structure

from random import randint


class LinkedListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values = None):
        self.head = None   # pointer to head of ll
        self.tail = None   # pointer to tail of ll
        self.length = 0    # length of ll
        if values:
            self.append_multiple_values(values)

    def __str__(self):
        current = self.head
        ll = []
        while current is not None:
            ll.append(current.value)
            current = current.next
        return 'LinkedList: ' + ' -> '.join(map(str, ll))

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        self.length += 1
        return self.tail

    def prepend(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        self.length += 1
        return self.head

    def delete_value(self, value):
        if self.head is None:
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        return self.head

    def append_multiple_values(self, values):
        for v in values:
            self.append(v)

    def generate(self, n, min_value, max_value):
        for _ in range(n):
            self.append(randint(min_value, max_value))


if __name__ == '__main__':
    lnklst = LinkedList([5]*5)
    #lnklst.generate(10, 0, 5)
    print lnklst
    for i in range(10):
        lnklst.delete_value(i)
    print lnklst.head, lnklst.tail
    print lnklst

