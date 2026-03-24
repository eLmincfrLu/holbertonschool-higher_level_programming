#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roma_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    sum = 0

    i = 0

    while i < len(roman_string):

        num = roma_dict[roman_string[i]]
        if i + 1 < len(roman_string) and num < roma_dict[roman_string[i + 1]]:
            sum += (roma_dict[roman_string[i + 1]] - num)
            i += 2
        else:
            sum += num
            i += 1

    return sum
