# Given a cell value 0 in mXn matrix make corresponding row & column 0


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    zero_matrix(matrix)