#!/usr/bin/python3
import sys

len_argv = len(sys.argv)
if len_argv < 2:
    print("{} arguments.".format(0))
else:
    print("{} argument:".format(len_argv))
    for i in range(1, len_argv):
        print("{}: {}".format(i, sys.argv[i]))