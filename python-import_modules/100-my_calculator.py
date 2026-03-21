#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    first = argv[1]
    second = argv[3]
    if argv[2] == "+":
        print("{} + {} = {}".format(first, second, add(int(first), int(second))))
    elif argv[2] == "-":
        print("{} - {} = {}".format(first, second, sub(int(first), int(second))))
    elif argv[2] == "*":
        print("{} * {} = {}".format(first, second, mul(int(first), int(second))))
    elif argv[2] == "/":
        print("{} / {} = {}".format(first, second, div(int(first), int(second))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
