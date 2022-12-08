#!/usr/bin/python3
def weight_average(my_list=[]):
    w_av = 0
    total = 0
    if not my_list or len(my_list) < 1:
        return w_av
    for x in my_list:
        w_av += (x[0] * x[1])
        total += x[1]
    w_av /= total
    return w_av
