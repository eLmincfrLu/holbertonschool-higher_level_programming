#!/usr/bin/python3
def no_c(my_string):
    siyah = list(my_string)
    new_string = ""
    for letter in siyah:
        if letter == "c" or letter == "C":
            continue
        else:
            new_string += letter
        return new_string
