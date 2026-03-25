#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list if they are integers.
    Returns the number of integers printed.
    """
    count = 0  # çapa çıxan integerlərin sayı
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # integer olmayan elementləri sadəcə keçirik
            continue
        except IndexError:
            # x list-in uzunluğundan böyükdürsə, try-except ilə dayandırırıq
            break
    print()
    return count