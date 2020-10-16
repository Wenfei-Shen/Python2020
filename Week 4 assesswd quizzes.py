## 1 ##

def student_pass(score1, score2, score3):
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    if (score1 >= 40) & (score2 >= 40) & (score3 >= 40):
        print('This student has passed.')
    elif (score1 >= 40) & (score2 >= 40) & ((score1 + score2 + score3) > 50*3):
        print('This student has passed.')
    elif (score1 >= 40) & (score3 >= 40) & ((score1 + score2 + score3) > 50*3):
        print('This student has passed.')
    elif (score2 >= 40) & (score3 >= 40) & ((score1 + score2 + score3) > 50*3):
        print('This student has passed.')
    else:
        print('This student has not passed.')



## 2 ##

# Create a function that determines whether the given year is a leap year.
def is_leap(year):
    year = int(year)
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    else:
        leap = False
    return leap


# Create a function to calculate the number of days since 1/1/1901 for a given date.
def days_since(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)

    # The total days passed since the start of the year at the beginning of each month for a non-leap year
    days_per_month_regular = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    # The total days passed since the start of the year at the beginning of each month for a leap year.
    days_per_month_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

    total_day = 0

    #  Year
    for i in range(1901, year):
        if (is_leap(i) == True):
            total_day += 366
        elif (is_leap(i) == False):
            total_day += 365

    # Month
    if (is_leap(year) == False):
        total_day += days_per_month_regular[month-1]
    elif (is_leap(year) == True):
        total_day += days_per_month_leap[month-1]

    # Day
    total_day += day - 1

    return total_day


# Create a function to find the day of the week of the given date.
def day_of_the_week(day, month, year):
    days = days_since(day, month, year)
    days_mod = days % 7

    if (days_mod <= 5):
        week_num = 2 + days_mod
    else:
        week_num = 1

    if week_num == 1:
        print('Monday')
    elif week_num == 2:
        print('Tuesday')
    elif week_num == 3:
        print('Wednesday')
    elif week_num == 4:
        print('Thursday')
    elif week_num == 5:
        print('Friday')
    elif week_num == 6:
        print('Saturday')
    elif week_num == 7:
        print('Sunday')



## 3 ##

def take_integral(A, X_1, X_2):
    N = len(A)
    co = [0] * N

    for i in range(0, N):
        co[i] = A[N-1-i]/(i+1) * ((X_2)**(i+1) - (X_1)**(i+1))

    return round(sum(co),2)


print(take_integral([-1, 2, 4.3], 0, 1))






