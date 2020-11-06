# 3

import numpy as np

def matrix_op(X, n, m):
    A = np.zeros((n,n))
    B = np.zeros((n,n))
    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = 2 * (i+X) + 3 * (j-X)
            B[i][j] = i - np.sqrt(j+X)
    C = np.linalg.matrix_power(B, m)
    D = np.dot(C, A)
    E = np.round(D, decimals=2)

    return E


print(matrix_op(6,2,3))
print(matrix_op(2,3,2))