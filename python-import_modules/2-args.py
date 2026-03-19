#!/usr/bin/python3
import sys

len_argv = len(sys.argv)
if __name__ == "__main__":
    if len_argv < 2:
        print("{} arguments.".format(0))
    else:
        if len_argv < 3:
            print("{} argument:".format(len_argv - 1))
        else:
            print("{} arguments:".format(len_argv - 1))
        for i in range(1, len_argv):
            print("{}: {}".format(i, sys.argv[i]))
