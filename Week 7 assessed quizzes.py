# 2
def float_swap(x):
    x = float(x)
    y = str(x)
    l = len(y)

    for i in range(0, l):
        if y[i] == '.':
            d = i
            break
    a = y[0:d]
    b = y[(d+1):l]
    z = [b, '.', a]
    result = ''.join(z)
    return result


print(float_swap(45.1234))
print(float_swap(0.1))
print(float_swap(37))
print(float_swap(1))
