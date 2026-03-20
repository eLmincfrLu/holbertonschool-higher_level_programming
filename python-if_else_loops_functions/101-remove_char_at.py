#!/usr/bin/python3
def remove_char_at(str, n):
    nev_str = list(str)
    if (n > len(nev_str) - 1):
        return str
    nev_str[n] = ""
    return ("".join(nev_str))
