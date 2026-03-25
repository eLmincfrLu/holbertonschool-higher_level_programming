#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list that are integers."""
    count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # integer olmayanları atla
            pass
        except IndexError:
            # list uzunluğunu keçdikdə dayandır
            break
        i += 1
    print()
    return count
