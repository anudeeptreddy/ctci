# Algorithm to check if a given string is a permutation of a palindrome


def is_palindrome_permutation(string):
    chars = {}
    str_list = list(string.replace(' ', ''))
    for ch in str_list:
        if ch in chars.keys():
            chars[ch] += 1
            if chars[ch] % 2 == 0:
                del chars[ch]
        else:
            chars[ch] = 1
    print chars
    return False if len(chars) > 1 else True


if __name__ == '__main__':
    print is_palindrome_permutation('tact coa')
