#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
#    new = []
#    for i in my_list:
#        if i not in new:
#            new.append(i)
#    for j in new:
#       res += j
    for i in set(my_list):
        res += i
    return res
