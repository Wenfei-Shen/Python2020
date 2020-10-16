## _________________ numpy ___________________##

import numpy as np

## EXAMPLE 1: complex number

def quad_real_roots(a, b, c):
    D = b**2 - 4*a*c
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    return x1, x2

print(quad_real_roots(2, -1, -3))

def quad_complex_roots(aR, bR, cR):
    a = np.complex(aR,0)
    b = np.complex(bR,0)
    c = np.complex(cR, 0)
    D = b ** 2 - 4 * a * c
    x1 = (-b + np.sqrt(D))/(2*a)
    x2 = (-b - np.sqrt(D))/(2*a)
    return x1, x2

print(quad_complex_roots(1, 2, 5))


## EXAMPLE 2: arrays
m1 = 0.5
b1 = 0.5
m2 = -1
b2 = 2

A = np.array([[-m1, 1], [-m2, 1]])  # 注意整个数列外面有一个[]
b = np.array([[b1], [b2]])
print(A)
print(np.shape(A)) # 查看数列形式

A_inv = np.linalg.inv(A)  # 求逆矩阵
print(A_inv)

X = np.dot(A_inv, b)  # 矩阵相乘
print(X)


## _________________ matplotlib ___________________##

import matplotlib.pyplot as plt
x_1 = np.linspace(-2, 6, 11)   # 生成随机数（起，止，数量）
print(x_1)
y_1 = m1*x_1 + b1

x_2 = x_1
y_2 = m2*x_2 + b2

plt.plot(x_1, y_1, color = 'magenta', linewidth = 3)
plt.plot(x_2, y_2)

plt.legend(['y = 0.5x+0.5 ', 'y=-x+2'])
plt.grid()
# plt.show()


