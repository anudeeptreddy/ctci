# Algorithm to rotate a given matrix by 90 degrees clockwise


def rotate_matrix(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    for layer in range(len(matrix) // 2):
        start, end = layer, n - 1 - layer
        for i in range(start, end):
            top = matrix[layer][i]                              # save top
            matrix[layer][i] = matrix[-i - 1][layer]            # top <- left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]  # left <- bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]  # bottom <- right
            matrix[i][- layer - 1] = top                        # right <- top
        return matrix


if __name__ == '__main__':
    matrix = [
        [01, 02, 03, 04, 05],
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],

    ]
    print rotate_matrix(matrix)

# Think about moving elements at indices in the directions below

# ------------->
# ^            |
# |            |
# |            |
# |            |
# |            V
# <-------------