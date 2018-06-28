from LinkedList import LinkedList


def sum_lists(ll1, ll2):
    if not ll1.head or not ll2.head:
        return None

    current1 = ll1.head if len(ll1) >= len(ll2) else ll2.head
    current2 = ll2.head if len(ll1) >= len(ll2)

    result = LinkedList([])
    carry = 0
    while current1 is not None:   # iterate through the longer ll
        value1 = current1.value
        value2 = current2.value if current2 is not None else 0

        sum = value1 + value2 + carry
        digit = sum % 10
        carry = sum // 10
        result.append(digit)

        if current1.next is None and carry > 0:   # add last carry if end of longer ll is reached
            result.append(carry)

        current1 = current1.next
        current2 = current2.next if current2 is not None else None

    return result


if __name__ == '__main__':
    ll1 = LinkedList([7, 1, 6])  # 617
    ll2 = LinkedList([5, 9, 2])  # 295
    print sum_lists(ll1, ll2)
