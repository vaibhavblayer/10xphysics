import numpy as np

a = [[1, 2], [3, 4]]
b = [[2, 3], [4, 5]]
c = []


mat1 = np.matrix(a)
mat2 = np.matrix(b)


print(mat1*mat2)


def matrix_mult(a, b):
    m = len(a)
    n = len(b[0])

    if m == n:
        ab = []
        for i in range(m):
            row = []
            for j in range(n):
                sum = 0
                for k in range(len(b)):
                    sum += a[i][k]*b[k][j]
                row.append(sum)
            ab.append(row)
        return ab

    else:
        return f'Invalid matrices'


print(matrix_mult([[2, 3], [3, 4]], [[2, 3], [2, 4]]))
