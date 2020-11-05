import numpy as np

def bi_section(f, a, b):
    '''
   this is a function that calculates a root for given functions "f" in the interval [a, b]
   inputs:
   f: the function for which we calculate the root.
   a: the beginning og the interval.
   b: the end of the interval
    '''
    while abs(b-a) > 1e-5:   # set the tolerance
        c = (a+b)/2
        if f(a)*f(c) < 0:
            b = c
        elif f(b)*f(c) < 0:
            a = c
        elif f(a) == 0:   # in case a or  b or c equals to zero.
            return a
        elif f(b) == 0:
            return b
        elif f(c) == 0:
            return c

    return (a+b)/2


def f(x):
    '''
    the function for which we are calculation the root.
    '''
    y = np.cos(x)
    return y

print(bi_section(f, 0, np.pi))