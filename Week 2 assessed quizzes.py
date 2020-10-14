## 1 ##

def my_function(x):
    x_new = int(x)
    a = x_new % 3
    b = x_new % 5
    c = x_new % 7
    y = [a, b, c]
    return y


## 2 ##

def temp_convert(deg_far):
    deg_cen = (5 / 9) * (deg_far - 32)
    print(round(deg_cen, 2))


## 3 ##

def every_other_num(x1, x2):
    my_list = list(range(x1, (1 + x2), 2))
    return my_list


## 4 ##

def time_converter(milliseconds):
    # Insert your code here...
    years = milliseconds // 31104000000
    months = (milliseconds - years * 31104000000) // 2592000000
    days = (milliseconds - years * 31104000000 - months * 2592000000) // 86400000
    hours = (milliseconds - years * 31104000000 - months * 2592000000 - days * 86400000) // 3600000
    mins = (milliseconds - years * 31104000000 - months * 2592000000 - days * 86400000 - hours * 3600000) // 60000
    secs = (milliseconds - years * 31104000000 - months * 2592000000 - days * 86400000 - hours * 3600000 - mins * 60000) // 1000
    ms = milliseconds - years * 31104000000 - months * 2592000000 - days * 86400000 - hours * 3600000 - mins * 60000 - secs * 1000

    # Print the result
    print(f'{years} years,')
    print(f'{months} months,')
    print(f'{days} days,')
    print(f'{hours} hours,')
    print(f'{mins} minutes,')
    print(f'{secs} seconds,')
    print(f'and {ms} milliseconds.')


