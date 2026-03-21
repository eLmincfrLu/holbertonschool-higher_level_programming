#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    first = sys.argv[1]
    second = sys.argv[3]
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(first, second, add(int(first), int(second))))
    elif sys.argv[2] == "":
        print("{} - {} = {}".format(first, second, sub(int(first), int(second))))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(first, second, mul(int(first), int(second))))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(first, second, div(int(first), int(second))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
