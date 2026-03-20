#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_listt = my_list.copy()
    for i in range(len(my_listt)):
        if my_listt[i] % 2 == 0:
            my_listt[i] = True
        else:
            my_listt[i] = False
    return my_listt
