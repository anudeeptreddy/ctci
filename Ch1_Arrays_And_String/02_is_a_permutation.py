# Algorithm to check if one string is a permutation of the other

counter = {}


def is_permutation(str1, str2):
    for ch in str1:
        if ch in counter.keys():
            counter[ch] += 1
            continue
        counter[ch] = 1

    for ch in str2:
        if ch not in counter.keys():
            return False
        counter[ch] -= 1
        if counter[ch] == 0:
            del counter[ch]

    return not counter


if __name__ == '__main__':
    print is_permutation('aacba', 'abcaa')
