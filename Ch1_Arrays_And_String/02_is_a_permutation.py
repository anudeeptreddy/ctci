# Algorithm to check if one string is a permutation of the other


def is_permutation(str1, str2):
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    return True if str1_sorted == str2_sorted else False


if __name__ == '__main__':
    print is_permutation('aacba', 'abcaa')