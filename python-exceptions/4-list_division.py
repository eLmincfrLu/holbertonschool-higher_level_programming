#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists and handles exceptions"""
    new_list = []

    for i in range(list_length):
        result = 0
        try:
            l1 = my_list_1[i]
            l2 = my_list_2[i]
            # Tip yoxlanışı
            if not isinstance(l1, (int, float)) or not isinstance(l2, (int, float)):
                print("wrong type")
            else:
                result = l1 / l2
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
