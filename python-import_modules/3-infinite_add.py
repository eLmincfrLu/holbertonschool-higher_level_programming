#!/usr/bin/python3
import sys

len_argv = len(sys.argv)

if __name__ == "__main__":
    result = 0
    for i in range(1, len_argv):
        result += int(sys.argv[i])
