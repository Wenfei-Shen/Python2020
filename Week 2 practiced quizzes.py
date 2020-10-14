
## 1 ##

def stringprint(string_argument):
    a = str(string_argument)  # 这一步很重要！转换输入数据的形式
    return print(a)
# stringprint('hello')


## 2 ##
def calculation_number1():
    answer = (0.87 + 3.14 + 0.63 + 297)**(3/2)
    return(answer)
# print(calculation_number1())


## 3 ##
def y_calculation():
    x = 0.45
    y = x**3 +3*x**2 +2*x + 1
    return y
# print(y_calculation())


## 4 ##
def hello_user():
    # you can ask for the user's name as below and store it in the variable "username"
    username = input("What is your name? ")
    return print('Hello '+str(username)+'!')  # 注意空格
# hello_user()


## 5 ##
def easy_sum():
    total = 0
    for i in range(1, 11):
        total = i + 1 + total
    print(total)
    return total
# easy_sum()


## 6 ##
import math

def circle_properties(r):
    # you can access the number pi using math module as below
    num_pi = math.pi
    # Insert your code to calculate the diameter, circumference, and area.
    d = 2 * r
    c = 2 * num_pi * r
    a = num_pi * r**2
    print("The diameter of the circle is "+str(d)+".")
    # Insert your code to print the same sentence for circumference and area.
    print("The circumference of the circle is " + str(round(c, 2)) + ".")  # 保留两位小数，输出的是字符！
    print("The area of the circle is " + str(round(a, 2)) + ".")
    return d, c, a
# circle_properties(2)


## 7 ##
def fibonacci():
    fib = [0] * 20
    # Insert your code here
    for i in range(2, 20):
        fib[1] = 1
        fib[0] = 0
        fib[i] = fib[i-1]+fib[i-2]
    print(fib)
    return fib
# fibonacci()


## 8 ##
def floats(a, b, c):
    x = [a, b, c]
    y = sorted(x)
    print(str(y[0])+', '+str(y[1])+', '+str(y[2]))
    return y
# floats(1,4,2)


