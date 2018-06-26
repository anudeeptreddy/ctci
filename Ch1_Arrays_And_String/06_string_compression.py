# Algorithm to implement string compression


def compress_string(string):
    str_len = len(string)
    new_str = []
    counter = 1
    for i in range(str_len - 1):
        curr = string[i]
        next = string[i+1]
        if curr == next:
            counter += 1
        else:
            new_str.append(string[i])
            new_str.append(counter)
            counter = 1

        if i + 1 == str_len - 1:
            new_str.append(string[i+1])
            new_str.append(counter)

    return ''.join(map(str, new_str)) if len(new_str) < str_len else string


if __name__ == '__main__':
    print compress_string('aabcccccaaad')