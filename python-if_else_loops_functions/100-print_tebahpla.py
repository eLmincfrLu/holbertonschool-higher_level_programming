#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(219-i) if i % 2 else chr(219-i).upper()), end="")
