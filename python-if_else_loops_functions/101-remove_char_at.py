#!/usr/bin/python3
def remove_char_at(str, n):
    nev_str = list(str)
    if (n > len(nev_str) - 1):
        return str
    if (-len(nev_str)) < abs(n) and n < 0:
        return str
    nev_str[n] = ""
    return ("".join(nev_str))

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))