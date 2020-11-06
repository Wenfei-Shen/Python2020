# 1

def primes_after(n):
   if n == 1:
       yield 2
   else:
        x = n - 1
        while True:
            x += 1
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                yield x


# 2
