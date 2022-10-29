import numpy as np


def range_square_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append(np.arange(i, i + n, 1))
    return np.array(matrix)
    # return np.array([np.arange(i, n + i) for i in range(n)])


ary = np.arange(6).reshape(2, 3)
print(ary)
print(ary[ary > 2])
ary[ary > 2] = ary[ary > 2] ** 2
print(ary)