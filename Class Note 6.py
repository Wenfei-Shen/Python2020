
# Topic one: list comprehensions
# creating a new from an existing list.

# example one
power_two = []
for n in range(12):
    if (2**n >= 100) and (2**n < 1000):
        power_two.append(2**n)
print(power_two)

power_two_lc = [2**n for n in range(12)]
print(power_two_lc)

power_two_lc2 = [2**n for n in range(12) if (2**n >= 100) and (2**n < 1000)]
print(power_two_lc2)


# example two

mysentence = 'Random fact i am a fan of Jam'
words = mysentence.split()
print(words)

ending_in_m = [word for word in words if word[-1] == 'm']
print(ending_in_m)


# Topic two: tuples
mytuple = (2, 4, 4, 6)
mylist = [2, 4, 4, 6]

# change the element
# Lists are mutable, but tuples are immutable.
mylist[2] = 5
print(mylist)
# mytuple[2] = 5


# Topic three: dictionary

# ugly approach: using lists
walnut_list = [['carb', 3.7], ['fat', 69.1], ['protein', 15.5]]
cereal_list = [['fat', 1.8], ['crab', 70], ['protein', 11]]

# dictionary
walnut_dic = {'carb': 3.7, 'fat': 69.1, 'protein': 15.5}   # in the same column - keys : values
print(walnut_dic['carb'])  # you do not need to remember the sort.
print(walnut_dic.keys())   # show the key.

cereal_dic = {'fat': 1.8, 'carb': 70, 'protein': 11}

compare = {'fat': [], 'carb': [], 'protein': []}

for x in walnut_dic.keys():
    if walnut_dic[x] > cereal_dic[x]:
        compare[x] = 'more'   # values can be numbers or strings
    else:
        compare[x] = 'less'

print('Walnuts have {} carb than cereal'.format(compare['carb']))


# Topic four: iterables and iterators
new_list = [1, 3, 5, 7]
itr_list = iter(new_list)   # make it a iterator

print(type(new_list))   # list is a iterables (the book)
print(type(itr_list))   # iterator is like a bookmark

print(next(itr_list))
print(next(itr_list))
print(next(itr_list))


# Topic five: generator
# a similar concept of iterator

# example 1
def natural_seq():
    num = 1
    while True:
        yield num   # instead of using return, use yield
        num += 1

gen_nat = natural_seq()
print(type(gen_nat))

print(next(gen_nat))
print(next(gen_nat))

print('I am chilling')
print(next(gen_nat))   # it starts from the previous number.


# example 2: Fibonacci sequence

def gen_fibo():
    numN = 0
    yield numN
    numN_1 = numN
    numN = 1
    yield numN
    while True:
        numN_2 = numN_1  # previous value
        numN_1 = numN   # present value
        numN = numN_2 + numN_1
        yield numN

my_gen_fibo = gen_fibo()

for x in my_gen_fibo:
    print(x)
    if x > 100:
        break


# generator comprehension and memory saving
# generator can save lots of memories

sqrd_num_lc = [x**2 for x in range(1000000)]   # list comprehension
sqrd_num_gc = (x**2 for x in range(1000000))   # generator comprehension

import sys

print(sys.getsizeof(sqrd_num_lc))  # 8697464
print(sys.getsizeof(sqrd_num_gc))  # 120 - memory efficient!


