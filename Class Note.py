######## Python Learning #######

## ________________________________ Week 1 ________________________________  ##
print('WEEK ONE')

## Print Function
print(456)
print('hello world')  # 文字要加引号，单双皆可

## Import Function)
import numpy as np  # 简化函数名
print(np.pi)  # 用 numpy.X 表示引用
print(np.cos(np.pi * 3))

## Variables
a = 0.5
b = 'Hello World'

##  ______________ Data Types ______________
print(type(a))
print(type(b))

# bool: True or False
c = 3 > 5  # 注意 ==, !=
print(c)
print(type(c))


## ________________________________  Week 2 ________________________________  ##
print('WEEK TWO')

## ______________ List  ______________
my_list = [1, 'love', [False, 1]]

# 求长度
my_len = len(my_list)
print(my_len)

# 增加值/合并 .append()
my_list.append('a new element')  # 不需要 my_list = my_list.append() !!!
print(my_list)

# 引用list中的值
print(my_list[0])

# 获得list中最后一个值
print(my_list[len(my_list)-1])
print(my_list[-1])

# 获得list中某一数组中的值
print(my_list[2][0])  # 注意：都是从0开始排序的！

# Slicing: my_list[start:stop:step]
new_list = [1,2,4,45,6,2,3,5346,5]
new_new_list = new_list[2:10:3]
print(new_new_list)

# str[]. capitalize() 一次一个值
cap_list = ['apple', 'banana', 'cook']
cap_new = []
cap_new.append(cap_list[0].capitalize())  #cao_list[想要的数据].capitalize(不要忘记括号)
print(cap_new)

##  ______________ loops ______________
cap_new2 = []
for i in cap_list:   # 这里i是cap_list中的一个元素
    cap_new2.append(i.capitalize())
print(cap_new2)

cap_new3 = []
for i in range(1,len(cap_list)+1):   # 这里i是数值range(1,len+1)
    cap_new3.append(cap_list[i-1].capitalize())
print(cap_new3)

# Fibonacci sequence
x = [1,1]
for i in range(0,9):
    x.append(x[i]+x[i+1])
print(x)


##  ______________ Functions ______________

def square_that_number(x):
    return x**2

y = square_that_number(7)
print(y)


import math
def f(x):
    y = (3*x-2)/math.sqrt(2*x+1)
    return y

