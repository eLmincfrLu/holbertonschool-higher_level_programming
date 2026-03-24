#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    count = 0
    for row in my_list:
        sum += row[0] * row[1]
        count += row[1]
    return sum / count
