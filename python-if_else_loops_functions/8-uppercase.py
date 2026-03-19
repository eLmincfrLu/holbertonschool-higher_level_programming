#!/usr/bin/python3
def uppercase(str):
    nev = ""
    for letter in str:
        if letter >= "a" and letter <= "z":
            nev = nev + chr(ord(letter)-32)
        else:
            nev = nev + letter
    return print("{}".format(nev))
