#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represent a class"""
    def __init__(self, size=0):
        """represent method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """represent method"""
        return self.size ** 2
