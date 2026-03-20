#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        first_a1 = 0
        first_a2 = 0
    else:
        first_a1 = tuple_a[0]

    if len(tuple_a) < 2:
            first_a2 = 0
    else:
            first_a2 = tuple_a[1]

    if len(tuple_b) < 1:
        first_b1 = 0
        first_b2 = 0
    else:
        first_b1 = tuple_b[0]

    if len(tuple_a) < 2:
            first_b2 = 0
    else:
        first_b2 = tuple_b[1]

    first = first_a1 + first_b1
    second = first_a2 + first_b2
    result = first, second
    return result
