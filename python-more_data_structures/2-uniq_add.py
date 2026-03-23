#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list2  = set(my_list)
    sum = 0
    for i in new_list2:
        sum += i
    return sum
