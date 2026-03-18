#!/usr/bin/python3
for number in range(97, 123):
    if chr(number) != "q" and chr(number) != "e":
        print("{}".format(chr(number)), end="")