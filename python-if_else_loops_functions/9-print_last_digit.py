#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        qaliq = number % 10
    else:
        qaliq = -10 + number % 10
    return print(qaliq)