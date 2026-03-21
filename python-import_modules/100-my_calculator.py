#!!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[3]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
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
