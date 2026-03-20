#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) - 1:
        return str
    nev_str = list(str)
    del nev_str[n]
    return "".join(nev_str)
