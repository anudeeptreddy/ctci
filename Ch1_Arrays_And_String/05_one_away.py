# Algorithm to check if the give two string are one edit away


def is_one_edit_away(left, right):
    left_str = list(left)
    right_str = list(right)
    chars = {}

    for ch in left_str:
        if ch in chars.keys():
            chars[ch] += 1
        else:
            chars[ch] = 1
    for ch in right_str:
        if ch in chars.keys():
            chars[ch] -= 1
            if chars[ch] == 0:
                del chars[ch]
        else:
            chars[ch] = 1

    # if length of remaining chars is > 2 indicates that at least 2
    # edits are required (or) if count of one char is > 1 then 2 edits
    # are required
    print chars
    if len(chars) <= 2:
        for key in chars:
            if chars[key] > 1:
                return False
    return False if len(chars) > 2 else True


if __name__ == '__main__':
    print is_one_edit_away('palessd', 'pale')
