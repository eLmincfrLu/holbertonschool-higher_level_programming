#!/usr/bin/python3
for num in range(1, 89):
    snum = str(num)
    if num < 10:
        print("0{}".format(num), end=", ")
    else:
        if snum[::-1] > snum:
            print("{}".format(num), end=", ")
print("89")
