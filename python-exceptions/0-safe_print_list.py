#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    
    new_list = []

    try:
        new_list = my_list[:x]
    except IndexError:
        new_list = my_list[:]
    
    stri = ""
    for i in new_list:
        stri += str(i)
    return int(stri)
