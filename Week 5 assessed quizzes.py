# 1

def collatz(m):
    '''
    Returns the number of elements of the Collatz
    sequence starting with m.
    '''
    A = [m]
    k = 0
    while m != 1:
        if m % 2 == 0:
            m = m/2
        elif m % 2 == 1:
            m = 3 * m + 1
        A.append(m)
        k += 1

    return k


# 2
# The problem asks you to find even-valued terms,
# which means that you'll need to find every value in the fibonacci sequence
# which can be divided by 2 without a remainder.


def even_sum(n):
    Fib = [0, 1]
    R = [0]
    i = 0
    while Fib[-1] <= n:
        Fib.append(Fib[i]+Fib[i+1])
        i += 1

    Fib_len = len(Fib) - 1

    for i in range(0, Fib_len):
        if Fib[i] % 2 == 0:
            R.append(Fib[i])

    return sum(R)


# 3

def lowest_integer(f, fmin):

   nmin = [1]
   i = 0
   while f(nmin[-1]) <= fmin:
       nmin.append(nmin[i]+1)
       i += 1

   return nmin[-1]



# 4

import numpy as np

def angle_dot(x, y):
    xy_dot = np.dot(x,y)
    unit_x = x / np.linalg.norm(x)
    unit_y = y / np.linalg.norm(y)
    dot_product = np.dot(unit_x, unit_y)
    angle = np.arccos(dot_product)
    angle_dgree = angle / np.pi * 180
    return round(xy_dot, 1), round(angle_dgree, 1)

