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




## ________________________________ Week 3 ________________________________  ##
print('WEEK THREE')

## Coonditional statements

# If loops
age = int(input('How old are you ?'))  # input function. int转换格式
my_license = input('Do you have a license? Y/N?')
# age = 14
# my_license = 'N'

#if my_license == 'Y' or my_license == 'Yes' or my_license == 'y':  #注意是==，不是=
if my_license in ["Y", "YES", "Yes", "y"]:
    if age >= 17:
        print('You can drive in the UK.')
    elif age >=15:
        print('You can drive with your parents.')
    else:
        print('You are too young to drive.')
elif my_license in ['N', 'NO', 'No', 'n']:
    print('You cannot drive. ')
else:
    print('Sorry, I did not get that.')

# 循环之间一定要对齐，不然会被认为是上面的循环！


# While loops

def GCD(m, n):
    '''
    return: the greatest common divisor of integer m and n.
    '''
    d = min(m, n)
    while m % d != 0 or n % d != 0:
        d = d - 1
    return d    
# print(GCD(40, 40))


# break: 达到条件即停止
# random walk

import time
import numpy as np

road_size = 2
max_step = 6

rng = np.random.default_rng()   # random number generator
pos = 0   # start from the middle of the road
steps = 0

while True:   # keep walking
    n = rng.choice([-1, 1])    # random choice: left(-1) or right (+1)
    pos += n                  # update position
    steps += 1                 # update number of steps

    if abs(pos) > road_size:   # if we went off the road, stop the loop early, display a message
        print('Went into the ditch! :(')
        break

    # show the step
    print('|' + ' '*(road_size + pos) + 'o' + ' '*(road_size - pos) + '|')
    time.sleep(.5)

    if steps >= max_step:
        print('Success! :)')
        break



