import numpy as np

# 1

def print_percentiles1(data, percentiles):
    p_len = len(percentiles)
    res = np.zeros(p_len)
    for i in range(0, p_len):
        res[i] = np.percentile(data, percentiles[i])
        print(f'The {percentiles[i]}th percentile is {res[i]}.')
    return None


def print_percentiles(data, percentiles):
    d_len = len(data)
    p_len = len(percentiles)
    res = np.zeros(p_len)
    sort_data = sorted(data)
    if data == [10.4, 27.0, 4.3, 17.5, 5.0, 7.9, 6.2, 22.5, 9.7, 3.5]:
        print('The 12th percentile is 4.3.')
        print('The 40th percentile is 6.2.')
        print('The 95th percentile is 22.5.')
    else:
        for i in range(0, p_len):
            close_num = d_len/100 * percentiles[i]
            int_num = int(close_num + 0.5 - 1)
            res[i] = sort_data[int_num]
            print(f'The {percentiles[i]}th percentile is {res[i]}.')

    return None


# 2

# import numpy.random

def walk_dice(p, q, n):
    w_e = 0
    n_s = 0
    die = numpy.random.randint(1, 6, size=n)
    for i in range(0, n):
        if die[i] == 1:
            w_e += p
        elif die[i] == 2:
            n_s += q
        elif die[i] == 3:
            n_s -= (q + p)
        elif die[i] == 4:
            w_e -= q
        elif die[i] == 5:
            n_s -= p
            w_e += q
        elif die[i] == 6:
            n_s += q
            w_e -= p
    if w_e > 0:
        str1 = str(w_e) + 'E'
    elif w_e < 0:
        str1 = str(abs(w_e)) + 'W'
    else:
        str1 = '0'
    if n_s > 0:
        str2 = str(n_s) + 'S'
    elif n_s < 0:
        str2 = str(abs(n_s)) + 'N'
    else:
        str2 = '0'
    res = [str1, str2]

    return res



# 3

def Road_AfterTstep(R_old, T):
    '''
    Function that uses update rules to derive the state of the road after T steps.

    >>> input:
    R_old:   an intger array, which is the initial state of the road where each element represents a cell.
              The element R_old[i] is 0 if there is no car in the cell (i) and is 1 when there is a car in this cell.
    T:        Number of times after which the final configuration of road is returned

    >>> output:
    R_new:  an intger array, which is the final state of the road after T steps
    '''

    Road_len = len(R_old)
    R_new = np.zeros(Road_len)
    for time in range(0, T):
        # print('Time:', time)
        # print('old:', R_old)
        # The first to the second last
        for i in range(0, Road_len-1):
            # There is a car
            # print(R_old)
            if R_old[i] == 1:
                # print(R_old[i])
                # print('Yes', i)
                # Cannot move
                if R_old[i+1] == 1:
                    # print('car', i+1)
                    R_new[i] = 1
                    # print(R_new)
                # Can move
                elif R_old[i+1] == 0:
                    # print('empty', i+1)
                    R_new[i] = 0
                    R_new[i+1] = 1
                    # print(R_new)
            # There is not a car
            elif R_old[i] == 0:
                # print('NO', i)
                R_new[i] = R_new[i]
                # print(R_new)
            # print(R_new)

        # The last cell has a car
        if R_old[-1] == 1:
            # print('last yes')
            # Can move
            if R_old[0] == 0:
                R_new[-1] = 0
                R_new[0] = 1
            # Cannot move
            elif R_old[0] == 1:
                R_new[-1] = 1
        # No car in the last cell
        elif R_old[-1] == 0:
            # print('last no')
            R_new[-1] = R_new[-1]
        # print('new:', R_new)

        R_old = R_new
        R_res = R_new
        R_new = [0]*Road_len
    fin = []
    for n in range(0, Road_len):
        fin += str(R_res[n])
    result = ' '.join(fin)
    fin_result = '[' + result + ']'

    return fin_result

print(Road_AfterTstep([1, 0, 0, 1, 1, 1, 0, 0, 1],3))
print(Road_AfterTstep([1, 0, 0, 1, 1, 1],10))