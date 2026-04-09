#!/usr/bin/python3
"""checker"""


def is_same_class(obj, a_class):
    """checker"""
    if obj == True:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
